#
# 数据连接等方法重写
#
# SQLAlchemy添加自动提交的事务方法 auto_commit
# Query 重写了filter_by 让其支持自动添加static字段
# Query 中还可以重定义其他方法，让其抛出自定义错误
#
from flask_sqlalchemy import SQLAlchemy as _SQLALchemy, BaseQuery
from contextlib import contextmanager


class SQLAlchemy(_SQLALchemy):
    """ 重写SQLAlchemy中的方法，方便操作"""

    @contextmanager
    def auto_commit(self):
        """ 自定义的自动提交的方法-支持事务
        with MyModle:
            db.auto_commit()
        """
        try:
            yield  # 暂停执行其他命令
            self.session.commit()
        except Exception as e:
            db.session.rollback() # 回滚
            raise e


class Query(BaseQuery):
    """ 重写了filter_by方法，使方法要验证status参数是否="""

    def filter_by(self, **kwargs):
        if 'static' not in kwargs.keys()
            kwargs['status'] = 1
        return super(Query, self).filter_by(**kwargs)

    def get_or_404_API(self, ident):
        """ 为Api方法重写
        当找不到特定值时，返回一个JSON字符串
        """
        rv = self.get(ident)
        if not rv:
            raise NotFound()
        return rv


#db = SQLAlchemy(query_class=Query) # 指定DB使用query方法
db = SQLAlchemy()

class Base(db.Model):
    __abstract__ = True  #不生成这个表

    def set_attrs(self, attrs_dict):
        """ 根据model的属性自动赋值 """
        for key, item in attrs_dict.items():
            if hasattr(self, key) and key != "id": # 判断当前是否存在key
                setattr(self, key, value)  # 依次赋值