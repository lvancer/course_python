# 数据库

# sqlite3

import sqlite3

# 数据库地址
# dbfile = "C:\\Users\\lin02\\AppData\\Roaming\\DBeaverData\\workspace6\\.metadata\\sample-database-sqlite-1\\Chinook.db"
# conn = sqlite3.connect(dbfile)          # 连接数据库
# cursor = conn.cursor()                  # 数据库指针，用于操作
# # 执行语句
# # cursor.execute("INSERT INTO foo (bar, baz) VALUES (1, 'a');")
# # if cursor.rowcount > 0:     # 有增加删除修改的行数
# #     print('修改了' + str(cursor.rowcount) + '行')
# # conn.commit()               # 执行
#
# # 查询语句
# cursor.execute("SELECT * FROM foo;")
# result = cursor.fetchall()
# print(result)
#
# cursor.execute("SELECT * FROM Track WHERE AlbumId = ? AND TrackId > ?;", (1, 1))
# print(cursor.fetchall())
#
# cursor.close()          # 关闭指针
# conn.close()            # 关闭连接


import pymysql
conn = pymysql.connect(
    host='127.0.0.1',       # 数据库地址
    port=3306,              # 数据库端口
    user='root',            # 用户名
    password='123456',      # 密码
    db='test',                # 数据库名
)

cursor = conn.cursor()
cursor.execute("SELECT * FROM test;")
print(cursor.fetchall())


