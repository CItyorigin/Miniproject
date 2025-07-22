from .models import db, User, Store, StoreStaff

def register_user(name, email, password):
    if User.query.filter_by(email=email).first():
        raise ValueError("이미 등록된 이메일입니다.")
    
    user = User(name=name, email=email)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return user


def create_store(name, address, contact):
    store = Store(name=name, address=address, contact=contact)
    db.session.add(store)
    db.session.commit()
    return store


def assign_staff(user_id, store_id, role):
    if role not in ['STAFF', 'MANAGER']:
        raise ValueError("역할은 STAFF 또는 MANAGER만 가능합니다.")
    
    staff = StoreStaff(user_id=user_id, store_id=store_id, role=role)
    db.session.add(staff)
    db.session.commit()
    return staff
