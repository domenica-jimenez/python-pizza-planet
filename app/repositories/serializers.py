from app.plugins import ma
from .models import Beverage, Ingredient, Order, OrderDetailIngredient, OrderDetailBeverage, Size


class IngredientSerializer(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = Ingredient
        load_instance = True
        fields = ('_id', 'name', 'price')

class BeverageSerializer(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = Beverage
        load_instance = True
        fields = ('_id', 'name', 'price')


class SizeSerializer(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = Size
        load_instance = True
        fields = ('_id', 'name', 'price')


class OrderDetailIndredientsSerializer(ma.SQLAlchemyAutoSchema):

    ingredient = ma.Nested(IngredientSerializer)

    class Meta:
        model = OrderDetailIngredient
        load_instance = True
        fields = (
            'ingredient_price',
            'ingredient'
        )

class OrderDetailBeverageSerializer(ma.SQLAlchemyAutoSchema):

    beverage = ma.Nested(BeverageSerializer)

    class Meta:
        model = OrderDetailBeverage
        load_instance = True
        fields = (
            'beverage_price',
            'beverage'
        )


class OrderSerializer(ma.SQLAlchemyAutoSchema):
    size = ma.Nested(SizeSerializer)
    detail_ingredient = ma.Nested(OrderDetailIndredientsSerializer, many=True)
    detail_beverage = ma.Nested(OrderDetailBeverageSerializer, many=True)

    class Meta:
        model = Order
        load_instance = True
        fields = (
            '_id',
            'client_name',
            'client_dni',
            'client_address',
            'client_phone',
            'date',
            'total_price',
            'size',
            'detail_ingredient',
            'detail_beverage'
        )
