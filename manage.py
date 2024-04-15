from flask.cli import FlaskGroup
from flask_migrate import Migrate
from flask_seeder import FlaskSeeder

from app import flask_app
from app.plugins import db
# flake8: noqa
from app.repositories.models import Ingredient, Beverage, Order, OrderDetailIngredient, OrderDetailBeverage, Size
from app.seeder.data_seeder import DataSeeder


manager = FlaskGroup(flask_app)

migrate = Migrate()
migrate.init_app(flask_app, db)

seeder = FlaskSeeder()
seeder.init_app(flask_app, db)

@manager.command('seeder', with_appcontext=True)
def seed():
    return DataSeeder().run()

@manager.command('delete', with_appcontext=True)
def seed():
    return db.drop_all()

if __name__ == '__main__':
    manager()
