# project/app/services.py

from .models import db, User, Store, Employee

def create_user(username, email, password):
    user = User(username=username, email=email, password=password)
    db.session.add(user)
    db.session.commit()
    return user

def create_store(name, location, owner_id):
    store = Store(name=name, location=location, owner_id=owner_id)
    db.session.add(store)
    db.session.commit()
    return store

def create_employee(name, role, store_id):
    employee = Employee(name=name, role=role, store_id=store_id)
    db.session.add(employee)
    db.session.commit()
    return employee
