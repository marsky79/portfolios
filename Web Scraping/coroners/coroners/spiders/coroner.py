import scrapy
from coroners.items import CoronersItem


#https://www.judiciary.uk/pfd-types/suicide-from-2015/
#https://www.judiciary.uk/prevention-of-future-death-reports/mohammed-akram-prevention-of-future-deaths-report/

#//*[@id="main-content"]/div[1]/div/article/div[1]/p[5]/text()[3]

class CoronerSpider(scrapy.Spider):
    name = "coroner"
    allowed_domains = ["judiciary.uk"]
    start_urls = ["https://www.judiciary.uk/pfd-types/suicide-from-2015/"]

    #Follow link cards
    def parse(self, response):
        for links in response.css('h3.card__title a::attr(href)').getall():
            yield response.follow(url=links, callback=self.parse_data)

        next_page = response.css('a.next.page-numbers::attr(href)').get()
        if next_page:
            yield response.follow(url=next_page, callback=self.parse)  

    def parse_data(self, response):
        item = CoronersItem()
        item['reff_id'] = response.css('#main-content > div:nth-child(1) > div > article > div.flow > p:nth-child(3)::text').get()
        item['coroner_name'] = response.css('#main-content > div:nth-child(1) > div > article > div.flow > p:nth-child(5)::text').get()
        item['report_sent_to'] = response.xpath('//*[@id="main-content"]/div[1]/div/article/div[1]/p[6]/text()[2]').get()
        item['coroner_concerns'] = response.xpath('//*[@id="main-content"]/div[1]/div/article/div[1]/figure/table/tbody/tr[6]/td[2]').get()

        yield item 