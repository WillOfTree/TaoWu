from flask import Blueprint 

# 创建当前view的视图
api = Blueprint("api", __name__)


@api.route('/')
def home():
    return '<h1>Hello, this is admin blueprint</h1>'