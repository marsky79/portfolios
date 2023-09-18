# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class OyoroomsItem(scrapy.Item):
    #define the fields for your item here like:
    nama_penginapan = scrapy.Field()
    alamat_penginapan = scrapy.Field()
    harga = scrapy.Field()
    amenities = scrapy.Field()
    
    
