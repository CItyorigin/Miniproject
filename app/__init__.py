from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash
from config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    print("🚀 시스템을 시작합니다.")
    print("어플을 만드는 중입니다.")
    
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from .models import User, Store, Employee

    @app.route('/')
    def index():
        return jsonify({
            'message': 'Welcome to My API!',
            'endpoints': {
                '/api/users/signup': 'User Signup',
                '/api/stores': 'Create Store',
                '/api/employees': 'Register Employee'
            }
        })

    # 회원가입
    @app.route('/api/users/signup', methods=['POST'])
    def signup_user():
        data = request.json
        if not data:
            return jsonify({"error": "No input data provided"}), 400

        try:
            first_name = data.get('first_name')
            last_name = data.get('last_name')
            email = data.get('email')
            password = data.get('password')
            address = data.get('address')
            contact = data.get('contact')
            gender = data.get('gender')

            if User.query.filter_by(email=email).first():
                return jsonify({"error": "Email already exists"}), 400

            hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
            new_user = User(
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=hashed_password,
                address=address,
                contact=contact,
                gender=gender
            )
            db.session.add(new_user)
            db.session.commit()

            return jsonify({"message": "User created successfully", "user_id": new_user.id}), 201

        except Exception as e:
            return jsonify({"error": str(e)}), 500

    # 매장 등록
    @app.route('/api/stores', methods=['POST'])
    def create_store():
        data = request.json
        if not data:
            return jsonify({"error": "No input data provided"}), 400

        try:
            name = data.get('name')
            address = data.get('address')
            contact = data.get('contact')

            new_store = Store(
                name=name,
                address=address,
                contact=contact
            )
            db.session.add(new_store)
            db.session.commit()

            return jsonify({"message": "Store created successfully", "store_id": new_store.id}), 201

        except Exception as e:
            return jsonify({"error": str(e)}), 500

    # 직원 등록
    @app.route('/api/employees', methods=['POST'])
    def register_employee():
        data = request.json
        if not data:
            return jsonify({"error": "No input data provided"}), 400

        try:
            user_id = data.get('user_id')
            store_id = data.get('store_id')
            employee_type = data.get('type')

            user = User.query.get(user_id)
            store = Store.query.get(store_id)

            if not user or not store:
                return jsonify({"error": "User or Store not found"}), 404

            from random import randint
            employee_code = randint(1000, 9999)

            new_employee = Employee(
                user_id=user_id,
                store_id=store_id,
                type=employee_type,
                code=employee_code
            )
            db.session.add(new_employee)
            db.session.commit()

            return jsonify({
                "message": "Employee registered successfully",
                "employee_id": new_employee.id,
                "employee_code": new_employee.code
            }), 201

        except Exception as e:
            return jsonify({"error": str(e)}), 500

    print("✅ 어플리케이션 생성이 완료되었습니다.")
    return app
