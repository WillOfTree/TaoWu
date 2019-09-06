# 
# forms表单样例
# 
from wtforms import *

class RegistrationForm(Form):
    user = StringField("username", [validators.Length(min=4,max=23)])