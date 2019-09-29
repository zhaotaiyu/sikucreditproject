# -*- coding: utf-8 -*-
import scrapy,datetime
from sikucreditproject.assist import getnum
from scrapy import FormRequest,Request
from sikucreditproject.items import *
import re

class SikucreditSpider(scrapy.Spider):
	name = 'sikucredit'
	allowed_domains = ['jzsc.mohurd.gov.cn']
	start_urls = ['http://jzsc.mohurd.gov.cn/']

	def start_requests(self):
		self.num = getnum()
		print(self.num)
		# cookies = {
		# 	'Hm_lvt_b1b4b9ea61b6f1627192160766a9c55c':'1566788653',
		# 	'JSESSIONID':'E1263431D91204C5E5916A08514856',
		# 	 'Hm_lpvt_b1b4b9ea61b6f1627192160766a9c55c':'1566802571'
		# }
		chengxin_url = 'http://jzsc.mohurd.gov.cn/asite/credit/record/query'
		for page in range (1,15):
			chengxin_formdata = {
				'$reload': '0',
				'$pg': str(page),
				'$pgsz': '10'
			}
			yield FormRequest(chengxin_url,formdata=chengxin_formdata,callback=self.parse_chengxin)
		black_url = 'http://jzsc.mohurd.gov.cn/asite/credit/record/blackList'
		for page in range (1,14):
			black_formdata = {
				'$reload': '0',
				'$pg': str(page),
				'$pgsz': '10'
			}
			yield FormRequest(black_url,formdata=black_formdata,callback=self.parse_black)
		punish_url = 'http://jzsc.mohurd.gov.cn/asite/credit/record/punishList'
		for page in range (1,6):
			punish_formdata = {
				'$reload': '0',
				'$pg': str(page),
				'$pgsz': '10'
			}
			yield FormRequest(punish_url,formdata=punish_formdata,callback=self.parse_punish)

	def parse_chengxin(self, response):
		tr_list = response.xpath("//table[@class='table_box credit_table']/tbody/tr")
		for tr in tr_list:
			record_num = tr.xpath("./td[1]/span/text()").extract_first()
			if record_num not in self.num and record_num:
				credit = SikucreditprojectItem()
				#诚信记录编号
				credit["record_num"] = record_num.strip()
				#诚信记录主体
				credit["record_main"] = str(tr.xpath("./td[2]/a/text()").extract_first()).strip()
				if credit["record_main"] =="None":
					credit["record_main"] = str(tr.xpath("./td[2]/text()").extract_first()).strip()
				#诚信主体id
				credit["main_id"] = str(tr.xpath("./td[2]/a/@href").extract_first()).strip().split("/")[-1]
				#决定内容
				credit["record_name"] = str(tr.xpath("./td[3]/text()[2]").extract_first()).strip()
				#事由
				credit["content"] = str(tr.xpath("./td[3]/div/a/@data-text").extract_first()).strip()
				#实施部门
				credit["department"] = str(tr.xpath("./td[4]/text()").extract_first()).strip()
				#文号
				credit["refer_num"] = str(tr.xpath("./td[4]/div/text()").extract_first()).strip()
				#决定日期
				credit["in_date"] = str(tr.xpath("./td[3]/div/span[2]/text()").extract_first()).strip().split("：")[-1]
				#发布有效期
				credit["out_date"] = str(tr.xpath("./td[5]/text()").extract_first()).strip()
				#原因
				credit["reason"] = str(tr.xpath("./td[1]/div/div/a/text()").extract_first()).strip()
				#主体类型
				credit["main_type"] = credit["record_num"].split("-")[1]
				#诚信类型
				credit["record_type"] = "bad"
				credit["created_at"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
				credit["updated_at"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
				yield credit

	def parse_black(self,response):
		tr_list = response.xpath("//table[@class='table_box credit_table']/tbody/tr")
		for tr in tr_list:
			record_num = tr.xpath("./td[1]/text()").extract_first()
			if record_num not in self.num and record_num:
				credit = SikucreditprojectItem()
				# 黑名单记录编号
				credit["record_num"] = record_num.strip()
				# 黑名单记录主体
				credit["record_main"] = str(tr.xpath("./td[2]/a/text()").extract_first()).strip()
				if credit["record_main"]  =="None":
					credit["record_main"] = str(tr.xpath("./td[2]/text()").extract_first()).strip()
				# 黑名单记录主体id
				credit["main_id"] = str(tr.xpath("./td[2]/a/@href").extract_first()).strip().split("/")[-1]
				# 黑名单认定依据
				credit["content"] = str(tr.xpath("./td[3]/text()[2]").extract_first()).replace("\n","").strip()
				credit["record_name"] = str(tr.xpath("./td[3]/text()[2]").extract_first()).replace("\n","").strip()
				# 文号
				credit["refer_num"] = str(tr.xpath("./td[3]/text()[2]").extract_first()).replace("\n","").strip()
				r = re.findall(".*（(\D+.*号)）",credit["refer_num"])
				if r:
					credit["refer_num"] = r[0]
				else:
					credit["refer_num"] = None
				# 认定部门
				credit["department"] = str(tr.xpath("./td[4]/text()").extract_first()).strip()
				# 列入黑名单日期	
				credit["in_date"] = str(tr.xpath("./td[5]/text()").extract_first()).strip()
				# 移出黑名单日期
				credit["out_date"] = str(tr.xpath("./td[6]/text()").extract_first()).strip()
				#原因
				credit["reason"] = str(tr.xpath("./td[1]/div/div/a/text()").extract_first()).strip()
				#主体类型
				credit["main_type"] = "QY"
				#诚信类型
				credit["record_type"] = "bad"
				credit["created_at"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
				credit["updated_at"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
				yield credit

	def parse_punish(self,response):
		tr_list = response.xpath("//table[@class='table_box credit_table']/tbody/tr")
		for tr in tr_list:
			record_num = tr.xpath("./td[1]/span/text()").extract_first()
			if record_num not in self.num and record_num:
				credit = SikucreditprojectItem()
				# 失信记录编号
				credit["record_num"] = record_num.strip()
				# 失信联合惩戒记录主体
				credit["record_main"] = str(tr.xpath("./td[2]/a/text()").extract_first()).strip()
				if credit["record_main"]  =="None":
					credit["record_main"] = str(tr.xpath("./td[2]/text()").extract_first()).strip()
				# 失信联合惩戒记录主体id
				credit["main_id"] = str(tr.xpath("./td[2]/a/@href").extract_first()).strip().split("/")[-1]
				# 法人姓名
				credit["legal_person"] = str(tr.xpath("./td[3]/div/span/text()").extract_first()).strip()
				# 法人身份证id
				credit["legal_person_idcard"] = str(tr.xpath("./td[3]/text()[2]").extract_first()).strip()
				# 列入名单事由
				credit["record_name"] = str(tr.xpath("./td[4]/text()[2]").extract_first()).strip()
				#备忘录
				credit["content"] = str(tr.xpath("./td[4]/div/a/@data-text").extract_first()).strip()
				# 文号
				credit["refer_num"] = str(tr.xpath("./td[4]/div/span/text()").extract_first()).strip().split("：")[-1]
				# 认定部门
				credit["department"] = str(tr.xpath("./td[5]/text()").extract_first()).strip()
				# 列入日期
				credit["in_date"] = str(tr.xpath("./td[6]/text()").extract_first()).strip().split("：")[-1]
				#原因
				credit["reason"] = str(tr.xpath("./td[1]/div/div/a/text()").extract_first()).strip()
				#主体类型
				credit["main_type"] = "QY"
				#诚信类型
				credit["record_type"] = "bad"
				credit["created_at"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
				credit["updated_at"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
				yield credit




		
