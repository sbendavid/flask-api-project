from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine  # Import create_engine
from config import config

app = Flask(__name__)  # Placeholder, not strictly needed here
app.config.from_object(config['development'])

engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])  # Create engine
db = SQLAlchemy(app=None, engine=engine)  # Initialize with engine

with db.app_context():
    try:
        db.create_all()
    except Exception as e:
        print(f"Error creating tables: {e}")
