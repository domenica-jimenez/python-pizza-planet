from app.services.templates.product_service import ProductService
from ..controllers import BeverageController

beverage = ProductService(BeverageController).template_service('beverage', __name__)
