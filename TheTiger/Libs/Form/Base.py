"""
    Form基础类
"""
from wtforms import Form

from Libs.Exception.ApiException import ApiFormError 

class BaseForm(Form):
    
    def __init__(self, data):
        # 初始化父类，父类会配置API
        super(BaseForm, self).__init__(data=data)


    # def validate(self):
    #     pass


    def validate_api(self):
        """
            新建一个会抛出异常的方法
        """
        valid = super(BaseForm, self).validate()
        if not valid:
            # form errors
            raise ApiFormError(msg=self.errors)
