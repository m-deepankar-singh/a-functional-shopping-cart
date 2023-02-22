from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager






app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myshop.db'
app.config['SECRET_KEY']='sjbjsbejsbejwnbjvwjewbeknw'



db = SQLAlchemy(app)
bcrypt=Bcrypt(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'customerLogin'
login_manager.needs_refresh_message_category='danger'
login_manager.login_message = u"Please login first"


from shop.admin import routes
from shop.products import routes
from shop.carts import carts
from shop.customers import routes