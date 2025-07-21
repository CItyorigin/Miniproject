from . import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255))
    contact = db.Column(db.String(20))
    gender = db.Column(db.String(10))

    employees = db.relationship('Employee', back_populates='user')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Store(db.Model):
    __tablename__ = 'store'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(255))
    contact = db.Column(db.String(20))
    is_active = db.Column(db.Boolean, default=True)

    employees = db.relationship('Employee', back_populates='store')


class Employee(db.Model):
    __tablename__ = 'employee'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    store_id = db.Column(db.Integer, db.ForeignKey('store.id'), nullable=False)
    type = db.Column(db.String(20), nullable=False)  # 'STAFF' or 'MANAGER'
    code = db.Column(db.Integer)

    user = db.relationship('User', back_populates='employees')
    store = db.relationship('Store', back_populates='employees')
