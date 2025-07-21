from flask import Blueprint, request, jsonify
from app.services import create_user, create_store, register_employee

main = Blueprint('main', __name__)

@main.route('/users', methods=['POST'])
def signup():
    data = request.get_json()
    try:
        user = create_user(
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
            email=data['email'],
            password=data['password'],
            address=data.get('address'),
            contact=data.get('contact'),
            gender=data.get('gender')
        )
        return jsonify({'id': user.id, 'email': user.email}), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

@main.route('/stores', methods=['POST'])
def add_store():
    data = request.get_json()
    store = create_store(
        name=data['name'],
        address=data.get('address'),
        contact=data.get('contact')
    )
    return jsonify({'id': store.id, 'name': store.name}), 201

@main.route('/employees', methods=['POST'])
def add_employee():
    data = request.get_json()
    try:
        employee = register_employee(
            user_id=data['user_id'],
            store_id=data['store_id'],
            emp_type=data['type'],
            code=data.get('code')
        )
        return jsonify({
            'id': employee.id,
            'user_id': employee.user_id,
            'store_id': employee.store_id,
            'type': employee.type,
            'code': employee.code
        }), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
