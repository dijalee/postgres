import os
from flask import Flask
from flask_jwt_extended import JWTManager

from app.users.route import bpUser
from app.auth.route import auth_bp
from app.prompt.route import prompt_bp
from app.group.route import group_bp


app = Flask(__name__)  
SECRET_KEY=os.environ.get('SECRET_KEY') or 'this is a secret'
app.config['SECRET_KEY']='apiREST'
jwt=JWTManager(app)




app.register_blueprint(bpUser,url_prefix='/users')
app.register_blueprint(auth_bp,url_prefix='/auth')
app.register_blueprint(prompt_bp,url_prefix='/prompt')
app.register_blueprint(group_bp,url_prefix='/group')
