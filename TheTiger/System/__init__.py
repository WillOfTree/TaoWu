import os
# import redis

###--------------------------
# 导入flask框架
from flask import Flask
from System.config import DevelopmentConfing
from System.config import static_dir, templates_dir, BASE_DIR

###--------------------------
# 创建项目应用，在这初始化一些参数
Flask_app = Flask(__name__,
        static_folder=static_dir,
        template_folder=templates_dir
    )
Flask_app.config.from_object(DevelopmentConfing)

