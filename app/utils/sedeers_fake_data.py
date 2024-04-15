
import random
from faker import Faker

def create_fake_users():
  fake = Faker()
  users = []
  for _ in range(10):
    users.append({
      "client_name": fake.name(),
      "client_dni": random.randint(1000000000, 9999999999),
      "client_address": fake.address(),
      "client_phone": random.randint(1000000000, 9999999999)
    })
  return users

size_seeder = [
  "Small", 
  "Medium", 
  "Large", 
  "Extra large", 
  "Extra extra large"
]

ingredient_seeder = [
  "Pepperoni", 
  "Mozzarella", 
  "Black olives", 
  "Mushrooms", 
  "Ham",
  "Bacon", 
  "Mozzarella", 
  "Red Onion", 
  "Green Pepper", 
  "Tomato"
]

beverage_seeder = [
  "Coca Cola", 
  "Pepsi", 
  "Sprite", 
  "7up",
  "Guitig",
  "Fanta",
  "San Felipe", 
  "Inca Cola", 
  "Water", 
  "Ice Tea"
]

user_seeder = create_fake_users()
