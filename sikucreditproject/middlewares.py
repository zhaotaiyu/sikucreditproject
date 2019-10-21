# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import time

from scrapy import signals
import random,datetime,pymongo
from .settings import *
import base64
from .utils import fetch_one_proxy

mongoclient=MONGOCLIENT
mongodatabase=MONGODATABASE
mongotable=MONGOTABLE
if "sikucreditproject.middlewares.KuaidailiMiddleware" in DOWNLOADER_MIDDLEWARES:
    fetch_time,proxy = fetch_one_proxy()
class MyUseragent(object):
    def process_request(self,request,spider):
        USER_AGENT_LIST = [
        'MSIE (MSIE 6.0; X11; Linux; i686) Opera 7.23',
        'Opera/9.20 (Macintosh; Intel Mac OS X; U; en)',
        'Opera/9.0 (Macintosh; PPC Mac OS X; U; en)',
        'iTunes/9.0.3 (Macintosh; U; Intel Mac OS X 10_6_2; en-ca)',
        'Mozilla/4.76 [en_jp] (X11; U; SunOS 5.8 sun4u)',
        'iTunes/4.2 (Macintosh; U; PPC Mac OS X 10.2)',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:5.0) Gecko/20100101 Firefox/5.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:9.0) Gecko/20100101 Firefox/9.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:16.0) Gecko/20120813 Firefox/16.0',
        'Mozilla/4.77 [en] (X11; I; IRIX;64 6.5 IP30)',
        'Mozilla/4.8 [en] (X11; U; SunOS; 5.7 sun4u)'
            ]
        agent = random.choice(USER_AGENT_LIST)
        request.headers['User_Agent'] =agent
class KuaidailiMiddleware(object):
    def __init__(self,username,password):
        self.username=username
        self.password=password
    def process_request(self, request, spider):
        proxy_url = 'http://%s:%s@%s' % (self.username, self.password, proxy)
        request.meta['proxy'] = proxy_url 
        auth = "Basic %s" % (base64.b64encode(('%s:%s' % (self.username, self.password)).encode('utf-8'))).decode('utf-8')
        request.headers['Proxy-Authorization'] = auth
    def process_response(self,request,response,spider):
        global fetch_time,proxy
        if response.status!=200:
            now_time = time.time() - 20
            if now_time>fetch_time:
                fetch_time,proxy = fetch_one_proxy()
        return response
    @classmethod
    def from_crawler(cls,crawler):
        return cls(
            username=crawler.settings.get("KUAI_USERNAME"),
            password=crawler.settings.get("KUAI_PASSWORD")
            )