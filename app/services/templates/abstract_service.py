from app.common.http_methods import GET, POST, PUT
from flask import Blueprint, jsonify

class AbstractService(Blueprint):
    def template_service(self, name, import_name):
        super().__init__(name, import_name)
        self.route('/', methods=POST)(self.create)
        self.route('/', methods=PUT)(self.update)
        self.route('/id/<_id>', methods=GET)(self.get_by_id)
        self.route('/', methods=GET)(self.get)
        return self
    
    def create(self) -> tuple:
        return jsonify({'error': f'Method not suported for {self.name}'}), 501
    
    def update(self) -> tuple:
        return jsonify({'error': f'Method not suported for {self.name}'}), 501
    
    def get_by_id(self) -> tuple:
        return jsonify({'error': f'Method not suported for {self.name}'}), 501
    
    def get(self) -> tuple:
        return jsonify({'error': f'Method not suported for {self.name}'}), 501

    