from System import Redprint

# 创建当前view的视图
api = Redprint("api")

# /api/get
@api.route('/get')
def home():
    return '<h1>Hello, this is admin blueprint</h1>'