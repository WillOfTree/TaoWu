"""
    Form基础类
"""
from wtforms import Form

from Libs import ApiFormError  # 自定义的异常类

class BaseForm(Form):
    def __init__(self):
        super(BaseForm.self).__init(data=data)

    def validate_for_api(self):
        """修改基本验证方法
        当验证失败，form会直接抛出ApiFormError

        form = ClientForm(data=data)
        form.validate_for_api()
        """
        valid = super(BaseForm, self).validate()
        if not valid:
            raise ApiFormError(msg=self.errors)
