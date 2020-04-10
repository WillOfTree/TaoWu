"""
    红图划分模块，使用蓝图区分项目
"""

class Redprint(object):

    def __init__(self, name): #接收红图的名字
        self.name = name
        self.mound = []

    def route(self, rule, **options):
        """
            route装饰器，rule = URL；
            **options = methods = ["GET"]
        """
        def decorator(f):
            # 这里记录函数名、路有规则、参数
            # 用于之后注册
            self.mound.append((f, rule, options))
            return f
        return decorator

    def register(self, bp, url_prefix:str=""):
        """
            红图注册方法：通道add_url_rule向蓝图注册方法
        """
        for f, rule, options in self.mound:
            # 如果没有endpoint的key，就返回f.__name__视图函数的名字
            endpoint = options.pop("endpoint", f.__name__)
            bp.add_url_rule(url_prefix + rule, endpoint, f, **options)