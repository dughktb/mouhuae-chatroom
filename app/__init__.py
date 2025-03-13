from flask import Flask
from .routes import main 
from .db import db
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__)
    
    # 配置数据库URI
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chatroom.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    
    migrate = Migrate(app, db)
    
    # 注册蓝图
    app.register_blueprint(main)
    
    with app.app_context():
        db.create_all()  # 确保数据库表被创建
    
    return app
