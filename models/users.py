from flask import request, jsonify
from models.user import User
from resources.schemas import UserSchema
from resources.db import db
from flask.views import MethodView
from flask_smorest import Blueprint , abort
from passlib.hash import pbkdf2_sha256
from flask_jwt_extended import create_access_token, jwt_required, get_jwt, get_jwt_identity, create_refresh_token
from werkzeug.security import generate_password_hash, check_password_hash
from blocklist import BLOCKLIST


user_bp = Blueprint('user_bp', __name__ ,description='User operations')


@user_bp.route('/register')
class UserRegister(MethodView):
    @user_bp.arguments(UserSchema)
    def post(self, user):
        if User.query.filter(User.username==user["username"]).first():
            abort(400, message="User already exists")
        
        
        db_user=User(username=user["username"], password=user["password"])
        print(db_user)
        db.session.add(db_user)
        db.session.commit()
        return {"message":"User created sucessfully"}, 201

@user_bp.route('/user/<int:user_id>')
class Userinfo(MethodView):
    @user_bp.response(200, UserSchema)
    def get(self, user_id):
        users = User.query.get_or_404(user_id)
        return users

    def delete(self, user_id):
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return {"message":"User deleted successfully"}, 200

@user_bp.route('/login', methods=['POST'])
class UserLogin(MethodView):
    @user_bp.arguments(UserSchema)
    def post(self, user):
        existing_user = User.query.filter_by(username=user["username"]).first()
        if existing_user and existing_user.check_password(user["password"]):
            access_token = create_access_token(identity=existing_user.id , fresh=True)
            refresh_token= create_refresh_token(identity=existing_user.id)
            return {"access_token": access_token , "refresh_token": refresh_token}, 200
        
        abort(401, message="Invalid username or password")
          
@user_bp.route('/logout')
class UserLogout(MethodView):
    @jwt_required()
    def post(self):
        jti = get_jwt()["jti"]
        BLOCKLIST.add(jti)
        return {"message":"Successfully logged out"}, 200