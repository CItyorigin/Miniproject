from flask import Blueprint, request, jsonify
from app.models import db, User, Store, Employee

bp = Blueprint('api', __name__, url_prefix='/api')


# 1. 회원가입
@bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
        return jsonify({'error': 'Missing required fields'}), 400

    if User.query.filter((User.username == username) | (User.email == email)).first():
        return jsonify({'error': 'User already exists'}), 409

    user = User(username=username, email=email)
    user.set_password(password)

    db.session.add(user)
    db.session.commit()

    return jsonify({'message': 'User created', 'user_id': user.id}), 201


# 2. 가게 등록
@bp.route('/stores', methods=['POST'])
def create_store():
    data = request.get_json()
    name = data.get('name')
    location = data.get('location')
    user_id = data.get('user_id')

    if not name or not user_id:
        return jsonify({'error': 'Missing required fields'}), 400

    store = Store(name=name, location=location, user_id=user_id)

    db.session.add(store)
    db.session.commit()

    return jsonify({'message': 'Store created', 'store_id': store.id}), 201


# 3. 직원 등록
@bp.route('/employees', methods=['POST'])
def create_employee():
    data = request.get_json()
    name = data.get('name')
    role = data.get('role')
    store_id = data.get('store_id')

    if not name or not store_id:
        return jsonify({'error': 'Missing required fields'}), 400

    employee = Employee(name=name, role=role, store_id=store_id)

    db.session.add(employee)
    db.session.commit()

    return jsonify({'message': 'Employee created', 'employee_id': employee.id}), 201
