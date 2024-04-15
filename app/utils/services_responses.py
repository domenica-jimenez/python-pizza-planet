from flask import jsonify

def services_response(data, error):
    response = data if not error else {'error': error}
    status_code = 200 if data else 404 if not error else 400
    return jsonify(response), status_code

def services_not_suported_response(self):
    return jsonify({'error': f'Method not suported for {self.name}'}), 501
