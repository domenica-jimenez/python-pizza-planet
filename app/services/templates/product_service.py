from app.services.templates.abstract_service import AbstractService
from flask import jsonify, request

class ProductService(AbstractService):
    def __init__(self, controller):
        self.controller = controller

    def create(self) -> tuple:
        product, error = self.controller.create(request.json)
        response = product if not error else {'error': error}
        status_code = 200 if not error else 400
        return jsonify(response), status_code
    
    def update(self) -> tuple:
        product, error = self.controller.update(request.json)
        response = product if not error else {'error': error}
        status_code = 200 if not error else 400
        return jsonify(response), status_code
    
    def get_by_id(self, _id: int) -> tuple:
        product, error = self.controller.get_by_id(_id)
        response = product if not error else {'error': error}
        status_code = 200 if product else 404 if not error else 400
        return jsonify(response), status_code
    
    def get(self) -> tuple:
        products, error = self.controller.get_all()
        response = products if not error else {'error': error}
        status_code = 200 if products else 404 if not error else 400
        return jsonify(response), status_code