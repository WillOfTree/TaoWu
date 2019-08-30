# -*- coding:utf-8 -*-
import json
import requests
import jwt

from datetime import datetime

#
# 配置参数
#

current_time = datetime.utcnow()
web_site_url = "http://127.0.0.1:8000"  # url请求

# 根据需求生成一个jwt值
# jwt_data = jwt.encode({  # jwt 编码后成的数据
#     "name": "bobby",
#     "id": 1,
#     "exp": current_time
# }, settings["secret_key"]).decode("utf8")

headers = {
    # "tokenid": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MjAsImV4cCI6MTU2NTA2MjQ1N30.Ew57QZq67oFc51sPTkUOekiPrzXsDorZDYFVl_kNz1U"
    "tokenid":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MSwiZXhwIjoxNTY1MDYzMjQ4fQ.Uh2-VjHG4nxTEqmbD-pr4mtEhsn6NH7pSdHMI9dTMsA"
}

# --------------------------------------------------------------

def one (
    current_time: str, web_site_url: str, headers: dict
) -> None:
    
    res = requests.post(web_site_url, headers=headers)
    print(res.status_code)
    # print(json.loads(res.text))
    print(res.text)

"""
上传图片
"""
def upload_image():
    files = {
        "image":open("./1.jpg", "rb")
    }
    data = {
        "name": "学前教育交流角",
        "desc": "这里是学前教育的交流中心，大家有什么问题可以一起来交流讨论！欢迎大家的加入！",
        "notice": "这里是学前教育的交流中心，大家有什么问题可以一起来交流讨论！欢迎大家的加入！",
        "category": "教育同盟"
    }
    res = requests.post(web_site_url, headers=headers, data=data, files=files)
    print(res.status_code)
    print(json.loads(res.text))

if __name__ == "__main__":
    # one(current_time, web_site_url, headers)
    upload_image()