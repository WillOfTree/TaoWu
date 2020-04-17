# 简单权限管理
#
# 权限填写
class UserScope(object):
    """ 权限最低，可操作的模块最少"""
    allow = []

class AdminScope(object):
    """ 权限最高，操作模块最多"""
    allow = []

    def __init__(self):
        self._add(UserScope())

    def _add(self, other):
        """ 将地权限的模块加入"""
        self.allow = self.allow + other.allow


# 用户权限验证
# 验证权限：
#   def verify_auth_token(token):
#       # scope权限， request.endpoint访问的控制器
#       is_in_scope(scope, reqest.endpoint)
#
def is_in_scope(scope:str, endpoint):
    """ 验证用户权限
    scope str 令牌中记录用户的权限
    endpoint str 要请求的路由 v1.super_get_user vi是因为注册在红土上的
    """
    # 通过反射创建一个对象
    scope = globals()[scope]()
    if endpoint in scope.allowapi:
        return True
    else:
        raise