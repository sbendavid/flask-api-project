from flask_bcrypt import generate_password_hash, check_password_hash
from uuid import uuid4
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.String, unique=True, nullable=False)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password_hash = db.Column(db.String, nullable=False)
    phone = db.Column(db.String)
    organisations = db.relationship('Organisation', secondary='user_organisation', back_populates='users')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password).decode('utf8')

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Organisation(db.Model):
    id = db.Column(db.String, primary_key=True, default=lambda: str(uuid4()))
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    users = db.relationship('User', secondary='user_organisation', back_populates='organisations')

class UserOrganisation(db.Model):
    __tablename__ = 'user_organisation'
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    organisation_id = db.Column(db.String, db.ForeignKey('organisation.id'), primary_key=True)
