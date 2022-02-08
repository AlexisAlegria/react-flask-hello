"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
import re
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from werkzeug.security import generate_password_hash, check_password_hash

api = Blueprint('api', __name__)

# Create a route to authenticate your users and return JWTs. The
# create_access_token() function is used to actually generate the JWT.

@api.route("/token", methods=["POST"])
def create_token():
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    # if email != "test" or password != "test":
    #     return jsonify({"message": "Bad username or password"}), 401

    user = User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password, password):
        response_body = {
        "message": "Access Denied. Please check your login details and try again.",
        }
        return jsonify(response_body), 400

    if user:
        access_token = create_access_token(identity=email)
        return jsonify(access_token=access_token)


@api.route("/signup", methods=["POST"])
def handle_signup():
    body = request.get_json()
    new_user = User(
        email = body['email'],
        password = generate_password_hash(body['password'], method='sha256'),
        )

    email = body['email']
    user = User.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database
    if user: # if a user is found, we want to redirect back to signup page so user can try again
        response_body = {
        "message": "Hi, Email address already exists",
        }
        return jsonify(response_body)

    try:
        password = body['password']
        reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
        pat = re.compile(reg)
        mat = re.search(pat, password)
        if mat:
            db.session.add(new_user)
            db.session.commit()
            response_body = {
            "message": "Hi, POST /users successfully response. Password is valid :)",
            }
        if not mat:
            response_body = {
            "message": "Invalid Password. it should have at least 6 characters, one Uppercase letter, numbers and one of these symbols: $ @ # %"
            }
            return jsonify(response_body), 400
    except:
        return "An error occurs adding user...", 400

    response_body = {
        "message": "Hi, User was created "
    }

    return jsonify(response_body), 200

@api.route("/users", methods=["GET"])
def handle_getUsers():
    query_users = User.query.all()
    query_users = list(map(lambda x: x.serialize(), query_users))
    response_body = {
        "message": "Hi, GET users response ",
        "users": query_users
    }

    return jsonify(response_body), 200

@api.route("/users/<int:id>", methods=["DELETE"])
def deleteUser(id):
    user_delete = User.query.get(id)
    if not user_delete:
        response_body = {
            "message": "Hi, DELETE /user response ",
            "user": "User not Found"
        }
        return jsonify(response_body), 200        
    db.session.delete(user_delete)
    db.session.commit()
    response_body = {
        "message": "Hi, DELETE /user response ",
        "user": "User deleted"
    }
    return jsonify(response_body), 200


@api.route("/hello", methods=["GET"])
@jwt_required()
def handle_hello():
    email = get_jwt_identity()
    body = {
        "message" : "Hello World! " + email
    }
    return jsonify(body)