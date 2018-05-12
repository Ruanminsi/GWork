import datetime
import random
import re

from app.models import Positiones, Users

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


def count(city, position):
	positions = Positiones.objects(city=city, positionName__icontains=position)
	return len(positions)


def count1(city):
	positions = Positiones.objects(city=city)
	return len(positions)
#
# print(count1('厦门'))
# print(count1('北京'))
# print(count1('上海'))
# print(count1('广州'))
# print(count1('深圳'))


def randomNum():
	numList = [0, 0, 0, 0, 0]
	numList[0] = random.randint(151, 352)
	numList[1] = random.randint(3301, 4102)
	numList[2] = random.randint(2120, 2645)
	numList[3] = random.randint(1885, 2110)
	numList[4] = random.randint(2018, 2219)
	return numList


def returnReport(key):
	exps = ['不限','1-3年','3-5年','5-10年']
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
	obj["title"] = key
	obj["pN"] = randomNum()
	return obj


def loginSituation():
	numlist = [0,0,0,0,0]
	d = datetime.datetime.now()
	d1 = d + datetime.timedelta(days=-1)
	d2 = d + datetime.timedelta(days=-2)
	d3 = d + datetime.timedelta(days=-3)
	d4 = d + datetime.timedelta(days=-4)
	dt = datetime.datetime.strftime(d, "%Y-%m-%d")
	dt1 = datetime.datetime.strftime(d1, "%Y-%m-%d")
	dt2 = datetime.datetime.strftime(d2, "%Y-%m-%d")
	dt3 = datetime.datetime.strftime(d3, "%Y-%m-%d")
	dt4 = datetime.datetime.strftime(d4, "%Y-%m-%d")
	us = Users.objects.all()
	lists = []
	for i in us:
		lists.append(i.last_login)
	for x in lists:
		t = str(x)
		if dt in t:
			numlist[4] += 1
		if dt1 in t:
			numlist[3] += 1
		if dt2 in t:
			numlist[2] += 1
		if dt3 in t:
			numlist[1] += 1
		if dt4 in t:
			numlist[0] += 1
	return numlist
loginSituation()