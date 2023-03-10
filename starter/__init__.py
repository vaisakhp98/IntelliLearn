from flask import Flask


from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
# from flask_session import Session
from flask_wtf import FlaskForm,CSRFProtect
from flask_mail import Mail



import torch
import torch.backends.cudnn as cudnn

app = Flask(__name__)

app.config['UPLOAD_FOLDER']="starter/static/uploads"

app.config['SECRET_KEY'] = '8ea2a86e42689205dde0ba81f31138b6'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///starter.db'

db = SQLAlchemy(app)

login_manager = LoginManager(app) 

# app.config['MAIL_SERVER'] = 'smtp.gmail.com'
# app.config['MAIL_PORT'] = 587
# app.config['MAIL_USE_TLS'] = True
# app.config['MAIL_USE_SSL'] = False
# app.config['MAIL_USERNAME'] = 'vismaya.fabstudioz@gmail.com'
# app.config['MAIL_PASSWORD'] = '66666'
# app.config['MAIL_DEFAULT_SENDER'] = 'vismaya.fabstudioz@gmail.com'
# mail = Mail(app)



from starter import routes

    
app.app_context().push()