from flask_smorest import Blueprint
from flask import request
from .models import User, Store, Employee, db

bp = Blueprint("Main", __name__, url_prefix="/")

@bp.route("/")
def index():
    return {
        "message": "붕어빵 통합 관리 프로그램에 오신 것을 환영합니다!",
        "docs": "/docs"
    }

@bp.route("/register", methods=["POST"])
@bp.arguments(schema={"type": "object", "properties": {"username": {"type": "string"}, "email": {"type": "string"}}, "required": ["username", "email"]})
@bp.response(201, description="회원 등록 완료")
def register_user(args):
    new_user = User(username=args['username'], email=args['email'])
    db.session.add(new_user)
    db.session.commit()
    return {"message": "User registered."}
