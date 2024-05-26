from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import secrets
from flask_migrate import Migrate
from resources.db import db
from flask_smorest import Api
from flask_marshmallow import Marshmallow
from models.user import User
from resources.schemas import UserSchema
from models.text_analysis import text_bp
from models.users import user_bp
from flask_swagger_ui import get_swaggerui_blueprint
from blocklist import BLOCKLIST
app = Flask(__name__)


# Setup the Flask-JWT-Extended extension
app.config["JWT_SECRET_KEY"]=  '35971377031082163320083521291083712705'
jwt=JWTManager(app)

app.config["API_TITLE"] = "Flask API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.2"
app.config["OPENAPI_URL_PREFIX"] = "/apidocs"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swaggerui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate=Migrate(app, db)
api=Api(app) #connect the app to the api

@jwt.token_in_blocklist_loader
def check_if_token_in_blocklist(jwt_header, jwt_payload):
    jti = jwt_payload['jti']
    return jti in BLOCKLIST

@jwt.unauthorized_loader
def unauthorized_callback(error):
    return jsonify({
        'message': 'Missing token',
        'error': 'authorization_required'
    }), 401

@jwt.invalid_token_loader
def invalid_token_callback(error):
    return jsonify({
        'message': 'Invalid token',
        'error': 'invalid_token'
    }), 401

@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    return jsonify({
        'message': 'Expired token',
        'error': 'token_expired'
    }), 401


SWAGGER_URL = '/swagger'
API_URL = '/apidocs/swagger.json'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "app"
    }
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
api.register_blueprint(user_bp)
api.register_blueprint(text_bp)
# Create database tables within application context
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)

