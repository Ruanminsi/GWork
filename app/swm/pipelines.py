class LagouPipeline(object):
    def open_spider(self,spider):
        self.fd = open(spider.name)
    def process_item(self, item, spider):
        line =""
        for key in ['name','catalog','workLocation','company','exp','degrees','property','temptation','salary','publishTime','workDuty','workRequire','detailLink']:
            line += item.get(key,"")+'\t'
        line += '\n'
        self.fd.write(line.encode('utf8'))
        return item
    def spider_closed(self, spider):
        self.fd.close()
