import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
from config import Config
from flask_dotenv import DotEnv
import logging
from logging.handlers import SMTPHandler
from flask_migrate import Migrate
aplication = Flask(__name__)
credentials = None
# mail_handler = SMTPHandler((Config.MAIL_SERVER, Config.MAIL_PORT), 'no-reply@' +
#                            Config.MAIL_SERVER, Config.ADMINS, 'microblog failure', credentials)
# mail_handler.setLevel(logging.ERROR)
# aplication.logger.addHandler(mail_handler)

db = SQLAlchemy(aplication)
env = DotEnv()
env.init_app(aplication, env_file=os.path.join(
    os.getcwd(), '.env'), verbose_mode=True)
aplication.config.from_object(Config)
mail = Mail(aplication)
migrate = Migrate(aplication, db)
login = LoginManager(aplication)
login.login_view = 'login'

from app import views, models