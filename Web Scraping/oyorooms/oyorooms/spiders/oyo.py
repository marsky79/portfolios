import scrapy
from oyorooms.items import OyoroomsItem


#https://www.oyorooms.com/id/allcities/
#https://www.oyorooms.com/id/hotels-in-ambon/
#https://www.oyorooms.com/id/81176/

#https://www.oyorooms.com/id/hotels-in-jakarta/

#https://www.oyorooms.com/id/hotels-in-jakarta/?page=1
#https://www.oyorooms.com/id/hotels-in-jakarta/?page=2
#Pagination response.css('a.c-nn640c.ListingPagination__pageContainer--page::attr(href)').getall())

class OyoSpider(scrapy.Spider):
    name = 'oyo'
    allowed_domains = ['www.oyorooms.com']
    start_urls = ['https://www.oyorooms.com/id/allcities/']

    #Follow city link in all cities
    def parse(self, response):
        for links in response.css('div.c-19rr7ql a::attr(href)').getall():
            yield response.follow(url='https://www.oyorooms.com' + links, callback=self.parse_link_hotels)

    #Follow hotels link in each cities
    def parse_link_hotels(self, response):      
        for links in response.css('a.c-nn640c::attr(href)').getall():
            yield response.follow(url='https://www.oyorooms.com' + links, callback=self.parse_hotel_data)        

        next_page = response.css('a.c-nn640c.ListingPagination__pageContainer--page::attr(href)').get()
        if next_page:  
            city_url = f"https://www.oyorooms.com{next_page}"
            yield response.follow(url=city_url, callback=self.parse_link_hotels)
            # yield response.follow(url=response.url, callback=self.parse_hotel_data)


    def parse_hotel_data(self, response):
        item = OyoroomsItem()
        item['nama_penginapan'] = response.css('h1.c-1wj1luj::text').get()
        item['alamat_penginapan'] = response.css('div.c-zo3nqe > h2:nth-child(1) > span:nth-child(1)::text').get()
        item['harga'] = response.css('span.listingPrice__finalPrice.listingPrice__finalPrice--black::Text').get()
        item['amenities'] = response.css('div.c-12w6zty::text').getall()

        yield item