from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # 配置数据库URI
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chatroom.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    
    # 注册蓝图
    from .routes import main
    app.register_blueprint(main)
    
    return app
