from app.services.templates.product_service import ProductService
from ..controllers import SizeController

size = ProductService(SizeController).template_service('size', __name__)
