# 自定义枚举类型

from enum import Enum

class ClientTypeEnum(enum):
    USER_EMAIL = 101 # 邮箱登录
    USER_MOBILE = 102 # 手机号登录

    USER_MINA = 103 # 小程序
    USER_WX = 104 # 微信公众号