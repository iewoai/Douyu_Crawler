# -*- coding: utf-8 -*-
from scrapy.pipelines.images import ImagesPipeline
import scrapy,os
from Douyu.settings import IMAGES_STORE as images_store

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DouyuPipeline(ImagesPipeline):
	def get_media_requests(self, item, info):
		image_link = item['imagelink']
		yield scrapy.Request(image_link)

# 改掉默认储存地址和图片名
	def item_completed(self, results, item, info):
		image_path = [x["path"] for ok, x in results if ok]
		os.rename(images_store + image_path[0],images_store + item["nickname"]+".jpg")
		return item
