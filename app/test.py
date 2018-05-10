import re
from app.models import Positiones

alist = []


def countAverage(city, position, exp):
	'''
	计算平均工资
	:param str city:
	:param str position:
	:param str exp:
	:return: int average
	'''
	positions = Positiones.objects(city=city, positionName__icontains=position, workYear=exp)
	total = 0
	result = 0
	for item in positions:
		data = re.findall(r'(\d+)', item.salary)
		if len(data) < 2:
			average = int(data[0])
		else:
			average = (int(data[0])+int(data[1]))/2
		alist.append(average)
		total = total + average
		if len(positions) == 0:
			result = 8
		else:
			result = total / len(positions)
	return result


s = countAverage('厦门', 'Python', '1-3年')


def count(city, position):
	positions = Positiones.objects(city=city, positionName__icontains=position)
	return len(positions)

def returnReport(key):
	exps = ['应届生','1-3年','3-5年','5-10年']
	citys = ['厦门', '北京', '上海', '广州', '深圳']
	numList = []
	averageList = []
	for city in citys:
		numList.append(count(city, key))
		for exp in exps:
			x = round(countAverage(city, key, exp), 1)
			averageList.append(x)
	obj = {}
	obj["x"] = averageList[0:4]
	obj["b"] = averageList[4:8]
	obj["s"] = averageList[8:12]
	obj["g"] = averageList[12:16]
	obj["s1"] = averageList[16:20]
	obj["number"] = numList
	return obj
