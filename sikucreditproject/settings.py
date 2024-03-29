# -*- coding: utf-8 -*-

# Scrapy settings for sikucreditproject project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'sikucreditproject'

SPIDER_MODULES = ['sikucreditproject.spiders']
NEWSPIDER_MODULE = 'sikucreditproject.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'sikucreditproject (+http://www.yourdomain.com)'

# Obey robots.txt rules
#ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.5
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  # 'Accept-Language': 'en',
  # 'Cookie': 'Hm_lvt_b1b4b9ea61b6f1627192160766a9c55c=1566788653; JSESSIONID=8999BC008D48A121F635CDAA5DECDCBC; Hm_lpvt_b1b4b9ea61b6f1627192160766a9c55c=1566790157'

}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'sikucreditproject.middlewares.SikucreditprojectSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'sikucreditproject.middlewares.MyUseragent': 543,
   # 'sikucreditproject.middlewares.KuaidailiMiddleware': 544,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'sikucreditproject.pipelines.SikucreditprojectPipeline': 300,
   'sikucreditproject.pipelines.PgsqlPipeline': 301,
   'sikucreditproject.pipelines.ScrapyKafkaPipeline': 302,
}

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
#PGSQL
PGSQL_URI="ecs-a025-0002"
PGSQL_DATABASE="cic_database"
PGSQL_PASS="sikuyi"
PGSQL_USER="postgres"
PGSQL_PORT=54321
#MONGO配置
MONGOCLIENT='mongodb://ecs-a025-0002:27017/'
MONGODATABASE='sikuyilog'
MONGOTABLE='sikucredit'
#abuyun代理配置
PROXYUSER="H7895G9300YN511D"
PROXYPASS="AC67F9AA92D6F49F"
PROXYSERVER="http://http-dyn.abuyun.com:9020"
#快代理配置
KUAI_USERNAME="zhao_tai_yu"
KUAI_PASSWORD="7av2i9t5"
RETRY_HTTP_CODES = [500, 502, 503, 504, 400, 403, 408, 429, 407]
HTTPERROR_ALLOWED_CODES = [302,301,503,502,400,429]
#KAFKA配置
BOOTSTRAP_SERVER="49.4.90.247:6667"
TOPIC="TOPIC_sikuyifinally"