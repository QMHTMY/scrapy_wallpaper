# -*- coding: utf-8 -*-

BOT_NAME = 'wallpaper'
SPIDER_MODULES = ['wallpaper.spiders']
NEWSPIDER_MODULE = 'wallpaper.spiders'

#USER_AGENT = 'wallpaper (+http://www.yourdomain.com)'
ROBOTSTXT_OBEY = True
ITEM_PIPELINES = {
    'wallpaper.pipelines.RenameImagesPipeline': 300,
}
IMAGES_STORE='/home/username/Downloads/scrapy/bingpic/' #请按照自己电脑修改位置
IMAGES_MIN_WIDTH=110
IMAGES_MIN_HEIGHT=110
