from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from src.controllers.error_controller import error_bp
from src.utils.db_utils import init_db

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///errors.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    CORS(app)

    init_db(app)

    app.register_blueprint(error_bp, url_prefix='/api/errors')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
