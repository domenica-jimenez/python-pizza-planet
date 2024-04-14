from app.services.templates.abstract_service import AbstractService
from flask import request
from app.utils.services_responses import services_response

class ProductService(AbstractService):
    def __init__(self, controller):
        self.controller = controller

    def create(self) -> tuple:
        product, error = self.controller.create(request.json)
        return services_response(product, error)
    
    def update(self, _id: int) -> tuple:
        product, error = self.controller.update(_id, request.json)
        return services_response(product, error)
    
    def get_by_id(self, _id: int) -> tuple:
        product, error = self.controller.get_by_id(_id)
        return services_response(product, error)
    
    def get(self) -> tuple:
        products, error = self.controller.get_all()
        return services_response(products, error)