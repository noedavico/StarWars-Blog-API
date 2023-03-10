"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Personajes, Planetas, Favoritos
#from models import Person
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)
#Configure la extensión Flask-JWT-Extended
app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!
jwt = JWTManager(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

#ENDOPOINT
#@app.route('/user', methods=['GET'])
#def handle_hello():

    #response_body = {
        #"msg": "Hello, this is your GET /user response "
    #}

    #return jsonify(response_body), 200

# obtiene los datos de todos los usuarios
@app.route('/user', methods=['GET'])
def handle_hello():
    
    #querys o consultas
    users_query = User.query.all()
    results = list(map(lambda item: item.serialize(),users_query))

    response_body = {
        "msg": "ok",
        "results": results
    }

    return jsonify(response_body), 200

# obtiene los datos de un usuario
@app.route('/user/<int:user_id>', methods=['GET'])
def get_info_user(user_id):
    user_query = User.query.filter_by(id=user_id).first()
##querys o consultas
    response_body = {
        "msg": "ok",
        "result": user_query.serialize()
    }

    return jsonify(response_body), 200

# obtiene los datos de todos los personajes
@app.route('/personajes', methods=['GET'])
def load_personajes():
    personajes_query = Personajes.query.all()
    results = list(map(lambda item: item.serialize(),personajes_query))
    ##querys o consultas
    response_body = {
        "msg": "ok",
        "results": results
    }

    return jsonify(response_body), 200

# obtiene los datos de un personaje
@app.route('/personajes/<int:personaje_id>', methods=['GET'])
def get_info_personajes(personaje_id):
    personajes_query = Personajes.query.filter_by(id=personaje_id).first()
##querys o consultas
    response_body = {
        "msg": "ok",
        "result": personajes_query.serialize()
    }

    return jsonify(response_body), 200

# obtiene los datos de todos los planetas
@app.route('/planetas', methods=['GET'])
def load_planetas():
    planetas_query = Planetas.query.all()
    results = list(map(lambda item: item.serialize(),planetas_query))
    ##querys o consultas
    response_body = {
        "msg": "ok",
        "results": results
    }

    return jsonify(response_body), 200

# obtiene los datos de un planeta
@app.route('/planetas/<int:planeta_id>', methods=['GET'])
def get_info_planetas(planeta_id):
    planetas_query = Planetas.query.filter_by(id=planeta_id).first()
##querys o consultas
    response_body = {
        "msg": "ok",
        "result": planetas_query.serialize()
    }

    return jsonify(response_body), 200

@app.route('/favoritos', methods=['GET'])
def load_favoritos():
    favoritos_query = Favoritos.query.all()
    results = list(map(lambda item: item.serialize(),favoritos_query))
    ##querys o consultas
    response_body = {
        "msg": "ok",
        "results": results
    }

    return jsonify(response_body), 200


# Create a route to authenticate your users and return JWTs. The
# create_access_token() function is used to actually generate the JWT.
@app.route("/login", methods=["POST"])
def login():
    # request_body = request.json
    # request_body =request.get_json()
    email = request.json.get("email", None)
    password = request.json.get("password", None)
# hacemos una consulta a la tabla para saber si el user existe
    user = User.query.filter_by(email=email).first()
#si no existe devuelvo msg
    if user is None:
        return jsonify({"msg": "User dosn´t exist"}), 404
    
    if email != user.email or password != user.password:
        return jsonify({"msg": "Bad email or password"}), 401
    access_token = create_access_token(identity=email)
    return jsonify(access_token=access_token)

# Cree una ruta para autenticar a sus usuarios y devolver JWT. El
# La función create_access_token() se usa para generar realmente el JWT..
@app.route("/profile", methods=["GET"])
@jwt_required()
def get_profile():
    # Accede a la identidad del usuario actual con get_jwt_identity

    current_user = get_jwt_identity()
    user = User.query.filter_by(email=current_user).first()
    print(user)
    return jsonify({"result":user.serialize()}), 200
# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
