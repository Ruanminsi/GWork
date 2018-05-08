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
	for item in positions:
		data = re.findall(r'(\d+)', item.salary)
		if len(data) < 2:
			average = int(data[0])
		else:
			average = (int(data[0])+int(data[1]))/2
		alist.append(average)
		total = total + average
	return total/len(positions)


s = countAverage('厦门', 'Python', '1-3年')


def count(city, position):
	positions = Positiones.objects(city=city, positionName__icontains=position)
	return len(positions)

exps = ['应届生','3年以下','3-5年','5-10年']
citys = ['厦门', '北京', '上海', '广州', '深圳']
key = 'Python'
numList = []
for city in citys:
	numList.append(count(city, key))

print(numList)