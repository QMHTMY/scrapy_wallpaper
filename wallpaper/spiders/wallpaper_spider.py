# -*- coding: utf-8 -*-
import sys
import scrapy
from wallpaper.items import ImageItem


class WallpaperSpiderSpider(scrapy.Spider):
    name = 'wallpaper'
    allowed_domains = ['bing.ioliu.cn']
    start_urls = ['https://bing.ioliu.cn']

    item = ImageItem()
    i = 0
    def parse(self, response):
        #step 1: get image title and url
        sel = response.xpath('//div[@class="description"]')
        ttls= sel.xpath('.//p[@class="calendar"]/em/text()').extract()
        self.item['titles'] = ttls

        lks = response.xpath('//div[@class="item"]/div/img/@src').extract()
        self.item['image_urls'] = lks
        yield self.item


        self.i += 1
        if self.i > 116: #116为https://bing.ioliu.cn页面最底部页数(1/xxx)中的xxx值，下载到最后一页就停止。
            sys.exit(0)

        #step 2: get next page url
        href = response.xpath('//div[@class="page"]/a[2]/@href').extract_first()
        next_url = response.urljoin(href)
        if next_url:
            yield scrapy.Request(next_url, callback=self.parse)
