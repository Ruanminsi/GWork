
import scrapy
from scrapy import Field

class LagouItem(scrapy.Item):
    name = Field()
    catalog = Field()       #类别
    workLocation = Field()  #工作地点
    detailLink = Field()    #具体链接
    publishTime = Field()   #发布日期
    workDuty = Field()      #工作职责
    workRequire = Field()   #工作要求
    company = Field()       #招聘公司
    exp = Field()           #经验要求
    degrees = Field()     #学历要求
    property = Field()      #工作性质
    temptation = Field()    #工作优势
    salary = Field()        #薪水
    
