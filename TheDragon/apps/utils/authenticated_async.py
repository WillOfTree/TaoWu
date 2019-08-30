# -*- coding:utf-8 -*-
#
# authenticated_async
# 
# 非阻塞异步验证
# ------------
#
# 用于代替tornado系统的authenticated方法
# 使用async/await对操作数据库等耗时操作进行改写
# 使用时注意对函数内标注位置进行修改，以适用系统
#   
#   1\使用jwt验证方式，如果使用其他方式，需要修改 TODO: #1,TODO: #2
#
#   2\如果需要跳转页面时，将self.set_status(401)设置为self.redirect( url )
#   setting.py:
#       login_url=”/login”
#   authenticated_async.py:
#       self.setting['login_url'] # 获取跳转字段的值

import functools
import jwt

# TODO: 根据实际情况引入需要使用的user表，用于查询用户是否存在
from apps.models.user import UserModel


def authenticated_async(method: str) -> None:
 
    @functools.wraps(method)
    async def wrapper(self, *args, **kwargs) -> None:
        # TODO: 根据前端header修改tokenid字段名称
        tsessionid = self.request.headers.get("tokenid", None)
        
        if tsessionid:
            """ 成功获取到前端tokenid值 """

            try:
                # TODO: #1
                # TODO: 确保secret_key,jwt_expire能正确获取
                send_data = jwt.decode(
                    tsessionid, self.settings["secret_key"], 
                    leeway=self.settings["jwt_expire"], 
                    options={"verify_exp": True} # 验证过期时间
                )
                user_id = send_data["id"] # 解析后获取用户ID


                try:
                    # TODO: #2
                    # TODO: 从数据库中获取用户信息
                    user = await self.db.get(UserModel, id=user_id)

                    # 经过我的分析，tornado.authenticated程序会调用current_user方法进行判断，
                    # current_user主要是加载重写的get_current_user方法
                    # 如果没有重写(get_current_user)就会返回None，调用@1，已重写调用 @2
                    # @1 authenticated方法就去去获取setting.py文件中的login_url参数，接着跳转到配置页面
                    # @2 调用被装饰的方法 
                    # self._current_user = user # 所有这句是无用的
                    await method(self, *args, **kwargs) # 调用自己的方法

                except UserModel.DoesNotExist as e:
                    # TODO: UserModel需要与用户表一致，不一致当未查询到用户时，会有一个错误无法捕捉
                    """ 当前用户未注册 """
                    self.set_status(401)

            except jwt.ExpiredSignatureError as e:
                """ jwt过期错误 """
                self.set_status(401)

        else:
            """ 没有tokenid字段错误 """
            self.set_status(401)

        self.finish({}) # 输出缓存

    return wrapper