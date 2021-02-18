from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy


bootstrap = Bootstrap()
db = SQLAlchemy()
def create_app():
    app = Flask(__name__)
    #解决’使用CSRF需要一个密钥‘问题
    app.config['SECRET_KEY'] = 'any secret string'
    app.config['SELECT_KEY'] = 'hard to guess string'

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost:3306/nation'
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

    db.init_app(app)
    bootstrap.init_app(app)

    #引入注册蓝本
    from .nationality import nationality as nationality_blueprint
    app.register_blueprint(nationality_blueprint)
    return app