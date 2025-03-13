from flask import Blueprint, request, jsonify
from .db import db
from .models import User, Message  # 确保导入路径正确
from werkzeug.security import generate_password_hash, check_password_hash

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return 'Welcome to mouhuae chatroom!'

@main.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid input'}), 400
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400
    if User.query.filter_by(username=username).first():
        return jsonify({'error': 'Username already exists'}), 400
    hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
    new_user = User(username=username, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully'}), 201

@main.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid input'}), 400
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400
    user = User.query.filter_by(username=username).first()
    if not user or not check_password_hash(user.password, password):
        return jsonify({'error': 'Invalid username or password'}), 400
    return jsonify({'message': 'Login successful'}), 200

@main.route('/chat', methods=['GET', 'POST'])
def chat():
    try:
        if request.method == 'POST':
            data = request.get_json()
            if not data:
                return jsonify({'error': 'Invalid input'}), 400
            username = data.get('username')
            content = data.get('content')
            if not username or not content:
                return jsonify({'error': 'Username and content are required'}), 400
            user = User.query.filter_by(username=username).first()
            if not user:
                user = User(username=username, password='default_password')
                db.session.add(user)
                db.session.commit()
            message = Message(user_id=user.id, content=content)
            db.session.add(message)
            db.session.commit()
            return jsonify({'message': 'Message sent!'}), 201
        else:
            messages = Message.query.all()
            return jsonify([{'username': msg.user.username, 'content': msg.content, 'timestamp': msg.timestamp} for msg in messages])
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@main.route('/favicon.ico')
def favicon():
    return '', 204  # 返回一个空响应体和状态码204，表示成功但没有内容