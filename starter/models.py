from starter import app
from starter import db,app
from starter import db,app,login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(id):
    return Register.query.get(int(id))


class Register(db.Model, UserMixin):
 id=db.Column(db.Integer, primary_key=True)
 email = db.Column(db.String(80))
 password = db.Column(db.String(80))
 usertype = db.Column(db.String(80))
 name = db.Column(db.String(80))
 age = db.Column(db.Integer)
 disability = db.Column(db.String(80))
 contact = db.Column(db.String(80))
 address = db.Column(db.String(80))
 status = db.Column(db.String(80),default='NULL')
 

class News(db.Model, UserMixin):
 id=db.Column(db.Integer, primary_key=True)
 subject = db.Column(db.String(80))
 news = db.Column(db.String(80))
 date = db.Column(db.String(80))
 image = db.Column(db.String(80))
 

class Query(db.Model, UserMixin):
 id=db.Column(db.Integer, primary_key=True)
 subject = db.Column(db.String(80))
 message = db.Column(db.String(80))
 uid = db.Column(db.String(80))
 response = db.Column(db.String(80))
 status = db.Column(db.String(80),default="NULL")

