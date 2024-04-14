from app.services.templates.product_service import ProductService
from ..controllers import IngredientController

ingredient = ProductService(IngredientController).template_service('ingredient', __name__)
