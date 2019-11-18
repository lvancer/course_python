# API调用

from api import juhe            # 从api包导入juhe模块
from datetime import datetime


def is_holiday(date=datetime.now()):
    info = juhe.calendar_day(date)      # 获得数据
    if info is not None and info['reason'] == 'Success':    # 验证数据正确
        result = info['result']
        if 'holiday' in result:
            return True         # 有holiday时，表示时假日
        else:
            return False
    return None


print(is_holiday())