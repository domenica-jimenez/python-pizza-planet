from app.services.templates.order_service import OrderService
from ..controllers import OrderController

order = OrderService(OrderController).template_service('order', __name__)
