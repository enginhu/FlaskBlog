import os


class Config(object):
    SECRET_KEY = "09fc4c35c731c7bb06d4092652a29cac"
    SQLALCHEMY_DATABASE_URI = "sqlite:///site.db?check_same_thread=False"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ADMINS = ['depodabekle@gmail.com', ]
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_POST = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USER')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
