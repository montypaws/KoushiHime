# -*- coding:utf-8 -*-

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CsrfProtect
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from flask.ext.login import LoginManager
from celery import Celery


db = SQLAlchemy()
csrf = CsrfProtect()
bootstrap = Bootstrap()
moment = Moment()
login_manager = LoginManager()
celery = Celery("tasks")


def create_app(config_name):
    """
    工厂函数，在服务运行前加载配置
    """
    app = Flask(__name__)
    from config import config
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    bootstrap.init_app(app)
    moment.init_app(app)
    csrf.init_app(app)
    login_manager.init_app(app)
    celery.conf.update(app.config)

    return app
