from typing import Any, List, Optional, Sequence

from sqlalchemy.sql import text, column, func, desc, extract

from .models import Beverage, db, Ingredient, Order, OrderDetailIngredient, OrderDetailBeverage, Size
from .serializers import (BeverageSerializer, IngredientSerializer, ma, OrderSerializer,
    SizeSerializer)


class BaseManager:
    model: Optional[db.Model] = None
    serializer: Optional[ma.SQLAlchemyAutoSchema] = None
    session = db.session

    @classmethod
    def get_all(cls):
        serializer = cls.serializer(many=True)
        _objects = cls.model.query.all()
        result = serializer.dump(_objects)
        return result

    @classmethod
    def get_by_id(cls, _id: Any):
        entry = cls.model.query.get(_id)
        return cls.serializer().dump(entry)

    @classmethod
    def create(cls, entry: dict):
        serializer = cls.serializer()
        new_entry = serializer.load(entry)
        cls.session.add(new_entry)
        cls.session.commit()
        return serializer.dump(new_entry)

    @classmethod
    def update(cls, _id: Any, new_values: dict):
        cls.session.query(cls.model).filter_by(_id=_id).update(new_values)
        cls.session.commit()
        return cls.get_by_id(_id)


class SizeManager(BaseManager):
    model = Size
    serializer = SizeSerializer


class IngredientManager(BaseManager):
    model = Ingredient
    serializer = IngredientSerializer

    @classmethod
    def get_by_id_list(cls, ids: Sequence):
        return cls.session.query(cls.model).filter(cls.model._id.in_(set(ids))).all() or []

class BeverageManager(BaseManager):
    model = Beverage
    serializer = BeverageSerializer

    @classmethod
    def get_by_id_list(cls, ids: Sequence):
        return cls.session.query(cls.model).filter(cls.model._id.in_(set(ids))).all() or []


class OrderManager(BaseManager):
    model = Order
    serializer = OrderSerializer

    @classmethod
    def create(cls, order_data: dict, ingredients: List[Ingredient], beverages: List[Beverage]):
        new_order = cls.model(**order_data)
        cls.session.add(new_order)
        cls.session.flush()
        cls.session.refresh(new_order)
        cls.session.add_all((OrderDetailIngredient(order_id=new_order._id, ingredient_id=ingredient._id, ingredient_price=ingredient.price)
                             for ingredient in ingredients))
        cls.session.add_all((OrderDetailBeverage(order_id=new_order._id, beverage_id=beverage._id, beverage_price=beverage.price)
                             for beverage in beverages))
        cls.session.commit()
        return cls.serializer().dump(new_order)

    @classmethod
    def update(cls):
        raise NotImplementedError(f'Method not suported for {cls.__name__}')


class IndexManager(BaseManager):

    @classmethod
    def test_connection(cls):
        cls.session.query(column('1')).from_statement(text('SELECT 1')).all()

class ReportManager():
    session = db.session
    serializer = IngredientSerializer

    @classmethod
    def get_report(cls):
        return {
            "most_required_ingredient": cls.get_most_required_ingredient_id(cls),
            "most_revenue_month": cls.get_most_revenue_month(cls),
            "best_customers": cls.get_best_customers(cls)
        }
    
    def get_most_required_ingredient_id(cls):
        serializer = cls.serializer()

        most_required_ingredient_id = cls.session.query(OrderDetailIngredient.ingredient_id, func.count(OrderDetailIngredient.ingredient_id)).group_by(OrderDetailIngredient.ingredient_id).order_by(desc(func.count(OrderDetailIngredient.ingredient_id))).first()

        return serializer.dump(Ingredient.query.get(most_required_ingredient_id.ingredient_id)) if most_required_ingredient_id else {}

    def get_most_revenue_month(cls):
        most_revenue_month = cls.session.query(extract('month', Order.date), func.sum(Order.total_price)).group_by(extract('month', Order.date)).group_by(extract('year', Order.date)).order_by(desc(func.sum(Order.total_price))).first()

        return {
            "month": most_revenue_month[0] or "No data available",
            "revenue": round(most_revenue_month[1], 2) or "No data available",
        } if most_revenue_month else {}
    
    def get_best_customers(cls):
        best_customers = cls.session.query(Order, func.sum(Order.total_price)).group_by(Order.client_dni).order_by(desc(func.sum(Order.total_price))).limit(3).all()

        return [{
            "client_name": order.client_name, 
            "client_dni": order.client_dni, 
            "client_phone": order.client_phone, 
            "client_address": order.client_address, 
            "total_price": round(total_price, 2)
            } for order, total_price in best_customers
        ] if best_customers else []
 