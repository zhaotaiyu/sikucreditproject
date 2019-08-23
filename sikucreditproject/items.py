# -*- coding: utf-8 -*-
import scrapy

class SikucreditprojectItem(scrapy.Item):
	main_id = scrapy.Field()
	record_main = scrapy.Field()
	main_type = scrapy.Field()
	record_name = scrapy.Field()
	record_type = scrapy.Field()
	reason = scrapy.Field()
	reason_type = scrapy.Field()
	content = scrapy.Field()
	department = scrapy.Field()
	publish_date = scrapy.Field()
	useful_date = scrapy.Field()
	in_date = scrapy.Field()
	out_date = scrapy.Field()
	legal_person = scrapy.Field()
	legal_person_idcard = scrapy.Field()
	source = scrapy.Field()
	relevant_project = scrapy.Field()
	relevant_person = scrapy.Field()
	area_code = scrapy.Field()
	url = scrapy.Field()
	status = scrapy.Field()
	created_at = scrapy.Field()
	creator = scrapy.Field()
	updated_at = scrapy.Field()
	record_num = scrapy.Field()
	refer_num = scrapy.Field()