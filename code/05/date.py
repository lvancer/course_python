# 时间

# 导入包
from datetime import datetime, timedelta

# 获取当前时间
now = datetime.now()
print('现在时间是' + str(now))

# 时间信息
year = now.year                 # 年
month = now.month               # 月
day = now.day                   # 日
hour = now.hour                 # 时
minute = now.minute             # 分
second = now.second             # 秒
microsecond = now.microsecond   # 毫秒
t = int(now.timestamp())        # 时间戳

print(str(year) + '-' + str(month) + '-' + str(day))
print('{}-{}-{}'.format(year, month, day))

# 时间格式化
import locale
locale.setlocale(locale.LC_CTYPE, 'chinese')    # 解决中文问题
print(now.strftime('%Y年%m月%d日 第%W周 星期%w'))

# 时间创建
date = datetime.strptime('2019年3月16日', '%Y年%m月%d日')
print(date)

# try:
#     birthday = input('输入你的生日(例：2019-03-16)? ')
#     birthday = datetime.strptime(birthday, '%Y-%m-%d')
#     print(birthday)
# except Exception as e:
#     print('时间格式输入错误')

birthday = datetime(year=2019, month=3, day=16)


# 时间计算
yesterday = now - timedelta(days=1)     # 昨天，减去一天
delta = now - yesterday                 # 时间差
print(delta.days)                       # 相差几天

