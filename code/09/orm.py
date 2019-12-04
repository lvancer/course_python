# ORM

# 创建连接

dbfile = "C:\\Users\\lin02\\AppData\\Roaming\\DBeaverData\\workspace6\\.metadata\\sample-database-sqlite-1\\Chinook.db"

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer  # 引入字段定义类

from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///' + dbfile)                     # sqlite3
# engine = create_engine('mysql+pymysql://root:123456@127.0.0.1/test')    # mysql
Base = declarative_base()


class Foo(Base):                # 继承基类

    __tablename__ = 'foo'       # 定义表名

    bar = Column(Integer, primary_key=True) # 定义字段，数字，主键必须定义
    baz = Column(String(20))                # 20长度的字符串


if __name__ == '__main__':
    Session = sessionmaker(bind=engine)     # 创建Session类
    # 添加
    # session = Session()         # 创建session
    # foo = Foo(bar=1, baz='a')   # 新增数据
    # session.add(foo)            # 添加
    # session.commit()            # 执行
    # session.close()             # 关闭session

    # 修改
    # session = Session()
    # foo = session.query(Foo).filter_by(bar=1).one()  # 条件查询
    # foo.baz = 'bb'      # 直接修改属性
    # session.add(foo)    # add保存
    # session.commit()
    # session.close()

    # 删除
    # session = Session()
    # foo = session.query(Foo).filter_by(bar=1).delete()
    # session.commit()
    # session.close()



