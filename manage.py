from flask.cli import FlaskGroup
from flask_migrate import Migrate

from app import flask_app
from app.plugins import db
# flake8: noqa
from app.repositories.models import Ingredient, Beverage, Order, OrderDetailIngredient, OrderDetailBeverage, Size


manager = FlaskGroup(flask_app)

migrate = Migrate()
migrate.init_app(flask_app, db)

if __name__ == '__main__':
    manager()
