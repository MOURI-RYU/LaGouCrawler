# -*- coding: utf-8 -*-

# Scrapy settings for LagouCrawler project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'LagouCrawler'

SPIDER_MODULES = ['LagouCrawler.spiders']
NEWSPIDER_MODULE = 'LagouCrawler.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'LagouCrawler (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Host': 'www.lagou.com',
    'Referer': 'https://www.lagou.com/',
    'Connection': 'keep-alive'
}

# 设置UA为随机挑选模式
RANDOM_UA_TYPE = 'random'

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'LagouCrawler.middlewares.LagoucrawlerSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'LagouCrawler.middlewares.LagoucrawlerDownloaderMiddleware': 543,
    # 在DownloaderMiddleware之前启用自定义的RandomUserAgentMiddlewaer
    'LagouCrawler.middlewares.RandomUserAgentMiddleware': 542,
    # 禁用框架默认启动的UserAgentMiddleware
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    #
    'LagouCrawler.middlewares.RandomProxyMiddleware': 601
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'LagouCrawler.pipelines.LagoucrawlerPipeline': 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# 用户名
USERNAME = '17386601610'
# 用户密码
PASSWORD = '175458778sd'

# 选择城市
CITY = '杭州站'

# 搜索职位
# JOB_KEYWORDS = 'Python 爬虫'

JOB_KEYWORDS = 'java后端'

# Mongodb地址
MONGO_URI = 'localhost'
# Mongodb库名
MONGO_DB = 'job'
# Mongodb表名
MONGO_COLLECTION = 'works'

# 代理列表
PROXY_LIST = [
    'http://113.128.9.11:23143',
    'http://49.85.3.252:35378',
    'http://220.162.155.7:42883',
    'http://121.227.76.45:31745',
    'http://123.55.93.229:21843',
    'http://113.128.30.242:30734',
    'http://114.218.249.134:47110',
    'http://182.39.4.9:48393',
    'http://115.205.10.153:22193',
    'http://110.82.81.120:33957'
]
