BOT_NAME = 'swm'

SPIDER_MODULES = ['swm.spiders']
NEWSPIDER_MODULE = 'swm.spiders'

DOWNLOAD_DELAY = 1.5
ITEM_PIPELINES = {
    'swm.pipelines.LagouPipeline': 400,
}
LOG_LEVEL = 'DEBUG'
DOWNLOAD_DELAY = 3
RANDOMIZE_DOWNLOAD_DELAY = True
CONCURRENT_ITEMS = 100
CONCURRENT_REQUESTS = 16
CONCURRENT_REQUESTS_PER_DOMAIN = 8
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2243.0 Safari/537.36'
DOWNLOADER_MIDDLEWARES = {
    'misc.middlewares.RotateUserAgentMiddleware': 400,
}
VALIDATE_PROXY=['http://60.209.166.172:8118', 'http://121.43.227.212:808', 
'http://113.87.90.218:53281', 'http://112.123.42.94:9745', 'http://175.42.102.252:8118',
'http://116.248.172.233:80', 'http://175.16.221.31:8118', 'http://171.36.182.180:8118',
'http://115.215.50.218:8118', 'http://171.126.12.9:80', 'http://113.205.0.23:8118', 
'http://106.58.152.171:80', 'http://59.63.178.203:53281', 'http://111.155.116.239:8123',
'http://117.90.34.87:8118', 'http://111.155.116.200:8123', 'http://61.183.176.122:53281',
'http://112.114.96.94:8118', 'http://58.49.122.30:53281', 'http://112.114.94.8:8118', 
'http://27.22.63.12:808', 'http://112.114.78.28:8118']

