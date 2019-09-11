# -*- coding: utf-8 -*-
import scrapy
import json
from Douyu.items import DouyuItem
# scrapy crawl douyu

class DouyuSpider(scrapy.Spider):
	name = 'douyu'
	allowed_domains = ['douyucdn.cn']
	#start_urls = ['http://douyucdn.cn/']
	baseURL = "http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset="
	offset = 0
	start_urls = [baseURL + str(offset)]


	def parse(self, response):
		#取出json文件
		data_list = json.loads(response.body)['data']
		# 若data为空则退出函数
		if not len(data_list):
			return
		for data in data_list:
			item = DouyuItem()
			item['nickname'] = data["nickname"]
			item['imagelink'] = data["vertical_src"]
			yield item

		self.offset += 20
		# print(self.baseURL + str(self.offset))
		yield scrapy.Request(self.baseURL + str(self.offset),callback = self.parse)
