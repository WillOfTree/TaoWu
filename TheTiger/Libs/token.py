#
# HTTPBasicAuth 是HTTP协议定义的账号密码传递方式
# 说明：
#   HTTPBasicAuth账号密码是保存在HTTP header中，除HTTPBasicAuth加密认证方式还有其他认证方式
# 加密方法：
#   Authorization: basic base64(account:password)
#
from flask import g

from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import BadSignature, SignatureExpired
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth() # 使用HTTPBasicAuth认证方式

@auth.verify_password
def verity_password(account, passwd):
    """ 验证方法，账号密码必须在HTTP header中，Authoritarian：basic base64(account:passwd)
    account 账号
    passwd  密码

    返回
        true 成功； false 失败，返回默认的错误认证错误

    使用方法：
        @web.route("/index", methods=["POST"]
        @auth.login_required
        def index():pass
    """
    #验证account, passwd正确性
    user_info = verify_auth_token(Token)
    if not user_info:
        return False
    else:
        g.user = user_info # 将用户数据保存在G变量中
        return True


def generate_auth_token(uid, ac_type=None, scope=None, exporation=7200):
    """ 生成令牌
    uid 用户id
    ac_type 登录类型
    taken = generate_auth_token(...)
    return jsonify({"token": token.decode("ascii")}), 201
    """
    s = Serializer(current_app.config['SECRET_KEY'], expires_in=exporation)
    return s.dumps({
        "uid": uid,
        "type": ac_type.value
    })


verity_return = namedtuple("token", ['UID', 'Name'])

def verify_auth_token(token):
    """ 验证token
    注意
    """
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        data = s.loads(token)
    except BadSignature:
        raise dict("token is invalid")
    except SignatureExpired:
        raise dict("token 过期")

    # 调用验证权限的方法-scope是权限标识
    # is_in_scope(scope, request.endpoint)
    # 使用namedtuple返回数据
    return verity_return(data['Uid'], data['Name'])
