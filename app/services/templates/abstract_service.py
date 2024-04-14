from app.common.http_methods import GET, POST, PUT
from flask import Blueprint, jsonify
from app.utils.services_responses import services_not_suported_response

class AbstractService(Blueprint):
    def template_service(self, name, import_name):
        super().__init__(name, import_name)
        self.route('/', methods=POST)(self.create)
        self.route('/<_id>', methods=PUT)(self.update)
        self.route('/id/<_id>', methods=GET)(self.get_by_id)
        self.route('/', methods=GET)(self.get)
        return self
    
    def create(self) -> tuple:
        return services_not_suported_response(self)
    
    def update(self, _id) -> tuple:
        return services_not_suported_response(self)
    
    def get_by_id(self, _id) -> tuple:
        return services_not_suported_response(self)
    
    def get(self) -> tuple:
        return services_not_suported_response(self)

    