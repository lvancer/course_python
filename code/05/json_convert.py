# json



content = """
{
	"reason":"Success",
	"result":{
		"data":{
			"holiday":"元旦",
			"avoid":"伐木.纳畜.破土.安葬.开生坟.嫁娶.开市.动土.交易.作梁.",
			"animalsYear":"兔",
			"desc":"2012年1月1日至3日放假调休，共3天，2011年12月31日（星期六）上班",
			"weekday":"星期日",
			"suit":"祭祀.开光.理发.整手足甲.安床.作灶.扫舍.教牛马.",
			"lunarYear":"辛卯年",
			"lunar":"腊月初八",
			"year-month":"2012-1",
			"date":"2012-1-1"
		}
	},
	"error_code":0
}
"""

import json
# json格式转换为python格式
data = json.loads(content)
print(data)
# python格式转换为json格式
content2 = json.dumps(data)
print(content2)
