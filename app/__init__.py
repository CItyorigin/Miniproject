# project/__init__.py
from flask import Flask, request, jsonify
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from . import config

# db와 migrate 객체 선언
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config.Config)

    # 데이터베이스 초기화
    db.init_app(app)
    migrate.init_app(app, db)

    # 인덱스 페이지 (API 안내)
    @app.route('/')
    def index():
        return jsonify({
            'message': 'Welcome to My API!',
            'endpoints': {
                '/users/signup': 'User Signup',
                '/stores': 'Create Store',
                '/employees': 'Register Employee'
            }
        })

    # route_bp 가져오기 (블루프린트 등록)
    from .routes import route_bp

    # ❗ 올바른 블루프린트 등록 방법
    app.register_blueprint(route_bp)

    return app
