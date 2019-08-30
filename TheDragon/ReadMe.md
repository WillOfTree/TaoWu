#--------------------
# 目录结构           -
#--------------------
Tornado     
  |-apps
  |  |-api     -- 应用目录
  |  |  |-- handler.py   # view
  |  |-models
  |  |  |-user.py        # orm
  |  |-utils   -- 自己的类库
  |  |  |--basehandler.py      # 公共handler
  |  |  |--decoratorsAsync.py  # 异步认证类
  |  |--urls.py          # 路由
  |  
  |-config     -- 配置文件
  |  |--application.py   # 初始化应用
  |  |--settings.py      # 配置信息
  |  |--urls.py          # 路由
  |  |--model.py         # orm
  |
  |-lib        -- 第三方库
  |  |--ueditor          # 富文本编辑器
  |
  |-statics    -- 静态文件
  |-templates  -- 模板
  |
  |-tool       -- 工具目录
  |   |--ini_db.py      # 数据库初始化文件
  |   |--HANDLER.md     # 跨域请求header
  |   |--TEST.py        # 测试请求文件
  |   |--upload.html    # aiox请求发送
  |
  |-server.py  -- 项目启动文件

#----------------------
# 引入模块             —
#----------------------
python 3.5以上版本
pip install tornado                      # 4以上
pip install --pre peewee-async aiomysql  # 安装peewee-async0.6.0以上版本
pip install redis
pip install pyjwt                        # json web token 
pip install aiofile                      # 异步文件存储 
pip install wtform                       # 表单验证


wtform-json    #表单验证
wtform         #表单验证

#----------------------
# resful Api
#----------------------