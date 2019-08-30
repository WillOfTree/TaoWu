# -*- coding=utf-8 -*-
#
# indexhandler template
#
# 简单的使用说明
# ------------
# import jwt  ##数据验证，xcrf防护
# from datetime import datetime   ##jwt需要的时间
# from apps.models.user import UserModel  ## orm类
# from apps.utils.authenticated_async import authenticated_async  ## 异步认证


from apps.utils.base_handler import BaseHandler


class IndexHandler(BaseHandler):

    # @authenticated_async
    async def get(self):
        a = self.get_argument("a", None)        
        
        self.render("index.html", a=a)


    # @authenticated_async
    async def post(self):
        self.write("POST_OK")
