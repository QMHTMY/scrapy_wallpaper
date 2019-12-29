# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from os.path import basename
from scrapy.http import Request 
from scrapy.pipelines.images import ImagesPipeline

class WallpaperPipeline(object):
    def process_item(self, item, spider):
        return item

class RenameImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        for img_url in item['image_urls']:
            img_type = basename(img_url).split('.')[1]  #jpeg, png
            img_idex = item['image_urls'].index(img_url)
            img_name = item['titles'][img_idex]         #2019-12-04

            img_name = ''.join(['BingWallpaper-',img_name,'.',img_type])
            yield Request(img_url, meta={'img_name': img_name})

    def file_path(self, request, response=None, info=None):
        return request.meta['img_name']
        #return basename(request.url)
