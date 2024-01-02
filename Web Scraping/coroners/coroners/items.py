# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CoronersItem(scrapy.Item):
    # define the fields for your item here like:
    reff_id = scrapy.Field()
    coroner_name = scrapy.Field()
    report_sent_to = scrapy.Field()
    coroner_concerns = scrapy.Field()
    pass
