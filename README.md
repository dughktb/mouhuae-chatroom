# Mouhuae Chatroom

这是一个简单的聊天室应用，使用Flask和SQLAlchemy构建。

## 安装

1. 克隆此仓库
2. 创建虚拟环境并激活
3. 安装依赖项
4. 初始化数据库
5. 运行应用

```bash
git clone <repository-url>
cd chatroom
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
flask db init
flask db migrate
flask db upgrade
python run.py
```

## 测试

1. 安装测试依赖项
2. 运行测试

```bash
pip install pytest
pytest
```

## API 端点

- `GET /` - 欢迎消息
- `GET /chat` - 获取所有消息
- `POST /chat` - 发送新消息

