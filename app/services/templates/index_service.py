from app.services.templates.abstract_service import AbstractService
from flask import jsonify

class IndexService(AbstractService):
    def __init__(self, controller):
        self.controller = controller
    
    def get(self) -> tuple:
        is_database_up, error = self.controller.test_connection()
        return jsonify({'version': '0.0.2', 'status': 'up' if is_database_up else 'down', 'error': error})