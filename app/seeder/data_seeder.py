import random
from faker import Faker
from datetime import datetime
from app.plugins import db
from app.test.utils.functions import get_random_price
from app.utils.sedeers_fake_data import beverage_seeder, ingredient_seeder, size_seeder, user_seeder
from app.repositories.models import (Beverage, Ingredient, Order, OrderDetailBeverage,
  OrderDetailIngredient, Size)

class DataSeeder():
    
    def run(self):
      self.size_seeder()
      self.ingredient_seeder()
      self.beverage_seeder()
      self.order_seeder()
      db.session.commit()
    
    def size_seeder(self):
      for index in range(5):
        db.session.add(
          Size(
            name=size_seeder[index], 
            price=get_random_price(10, 20)
          )
        )
    
    def ingredient_seeder(self):
      for index in range(10):
        db.session.add(
          Ingredient(
            name=ingredient_seeder[index], 
            price=get_random_price(10, 20)
          )
        )
    
    def beverage_seeder(self):
      for index in range(10):
        db.session.add(
          Beverage(
            name=beverage_seeder[index], 
            price=get_random_price(10, 20)
          )
        )
    
    def order_seeder(self):
      for index in range(100):
        fake = Faker()
        size = random.randint(1, 5)
        user = user_seeder[random.randint(0, 9)]
        db.session.add(
          Order(
            client_name=user.get('client_name'),
            client_dni=user.get('client_dni'),
            client_address=user.get('client_address'),
            client_phone=user.get('client_phone'),
            date=fake.date_time_between(datetime(2023,1,1), datetime(2023,4,30)),
            total_price=self.order_price_seeder(index+1, size),
            size_id=size,
          )
        )
    
    def order_price_seeder(self, order, size):
      return Size.query.get(size).price + self.order_ingregients_seeder(order) + self.order_beverages_seeder(order)
    
    def get_list_unique_ids(self):
      item_list = []
      for _ in range(random.randint(0, 10)):
        id_item = random.randint(1, 10)
        while id_item in item_list:
          id_item = random.randint(1, 10)
        item_list.append(id_item)
      return item_list
    
    def order_ingregients_seeder(self, order):
      ingredients_price = 0
      list_ingredients = self.get_list_unique_ids()
      for ingredient in list_ingredients:
        price = Ingredient.query.get(ingredient).price
        db.session.add(OrderDetailIngredient(
            ingredient_price=price,
            order_id=order,
            ingredient_id=ingredient
          )
        )
        ingredients_price += price
      return ingredients_price
  
    def order_beverages_seeder(self, order):
      beverage_price = 0
      list_beverages = self.get_list_unique_ids()
      for beverage in list_beverages:
        price = Beverage.query.get(beverage).price
        db.session.add(OrderDetailBeverage(
            beverage_price=price,
            order_id=order,
            beverage_id=beverage
          )
        )
        beverage_price += price
      return beverage_price
