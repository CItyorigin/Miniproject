from flask import request, jsonify
from flask_smorest import Blueprint as SmorestBlueprint
from app.services import create_user, create_store, register_employee

# Employee, Store, User 관련 API를 담당할 Blueprint 정의
route_bp = SmorestBlueprint('route_v1', __name__, url_prefix='/api')

# Swagger 문서화 및 API 스펙을 위한 데코레이터
@route_bp.route('/employees', methods=['POST'])
def register_employee_route():
    """
    Register an Employee in a store
    ---
    description: Register an employee with user_id, store_id, and employee type.
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            user_id:
              type: integer
              example: 1
            store_id:
              type: integer
              example: 1
            type:
              type: string
              example: "Manager"
    responses:
      201:
        description: Employee registered successfully
      400:
        description: Invalid input data provided
      404:
        description: User or Store not found
    """
    data = request.json
    response, status = register_employee(data)
    return jsonify(response), status


@route_bp.route('/stores', methods=['POST'])
def create_store_route():
    """
    Create a Store
    ---
    description: Create a new store with name, address, and contact details.
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
              example: "My Store"
            address:
              type: string
              example: "123 Main St"
            contact:
              type: string
              example: "+1 555-555-5555"
    responses:
      201:
        description: Store created successfully
      400:
        description: Invalid input data provided
    """
    data = request.json
    response, status = create_store(data)
    return jsonify(response), status


@route_bp.route('/users/signup', methods=['POST'])
def signup_user():
    """
    Sign Up a User
    ---
    description: Create a new user with name, email, password, and contact details.
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            first_name:
              type: string
              example: "John"
            last_name:
              type: string
              example: "Doe"
            email:
              type: string
              example: "john.doe@example.com"
            password:
              type: string
              example: "password123"
            address:
              type: string
              example: "123 Main St"
            contact:
              type: string
              example: "+1 555-555-5555"
            gender:
              type: string
              example: "Male"
    responses:
      201:
        description: User created successfully
      400:
        description: Invalid input data provided or email already exists
    """
    data = request.json
    response, status = create_user(data)
    return jsonify(response), status
