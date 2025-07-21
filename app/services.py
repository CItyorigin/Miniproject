from .models import User, Store, Employee
from . import db

def create_user(first_name, last_name, email, password, address=None, contact=None, gender=None):
    if User.query.filter_by(email=email).first():
        raise ValueError("이미 존재하는 이메일입니다.")
    user = User(
        first_name=first_name,
        last_name=last_name,
        email=email,
        address=address,
        contact=contact,
        gender=gender
    )
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return user

def create_store(name, address=None, contact=None):
    store = Store(
        name=name,
        address=address,
        contact=contact,
        is_active=True
    )
    db.session.add(store)
    db.session.commit()
    return store

def register_employee(user_id, store_id, emp_type, code=None):
    if emp_type not in ['STAFF', 'MANAGER']:
        raise ValueError("직원 유형은 'STAFF' 또는 'MANAGER'만 가능합니다.")
    # user, store 존재 여부 체크
    user = User.query.get(user_id)
    store = Store.query.get(store_id)
    if not user or not store:
        raise ValueError("유효하지 않은 User ID 또는 Store ID입니다.")

def employee = Employee(
        user_id=user_id,
        store_id=store_id,
        type=emp_type,
        code=code
    )
    db.session.add(employee)
    db.session.commit()
    return employee
