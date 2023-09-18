import scrapy
from lamudi.items import LamudiItem



class LamudihouseSpider(scrapy.Spider):
    name = 'house'
    allowed_domains = ['www.lamudi.co.id']
    start_urls = ['http://www.lamudi.co.id/house/buy/']
    
    def parse(self, response):
       for links in response.css('a.ListingCell-moreInfo-button-v2_redesign::attr(href)').getall():
            yield response.follow(url=links, callback=self.parse_rumah)
            
            next_page = response.css('div.next a::attr(href)').get()
            if next_page:
                yield response.follow(url=next_page, callback=self.parse)
        
    def parse_rumah(self, response):
        item = LamudiItem()
        item['title'] = response.css('h1.Title-pdp-title::text').get().replace('\n','').strip()     
        item['lokasi'] = response.css('h3.Title-pdp-address::text').getall()[1].strip().replace('\n','').replace(',','')
        item['harga'] = response.css('div.Title-pdp-price span::text').get().strip()
        item['keterangan'] = response.css('div.ellipsis::text').getall()
        item['rincian'] = response.css('div.last::text').getall()

        #yield item

#############################
        # item['column1'] = response.css('div.last::text').getall()[0].strip() 
        # if ['column1'] == IndexError:
        #     print('NA')
        # item['column2'] = response.css('div.last::text').getall()[1].strip() 
        # if ['column2'] == IndexError:
        #     print('NA')
        # item['column3'] = response.css('div.last::text').getall()[2].strip()
        # if ['column3'] == IndexError:
        #     print('NA')       
        # item['column4'] = response.css('div.last::text').getall()[3].strip() 
        # if ['column4'] == IndexError:
        #     print('NA')  
        # item['column5'] = response.css('div.last::text').getall()[4].strip()
        # if ['column5'] == IndexError:
        #     print('NA')        
        # item['column6'] = response.css('div.last::text').getall()[5].strip()
        # if ['column6'] == IndexError:
        #     print('NA')   
        # item['column7'] = response.css('div.last::text').getall()[6].strip()
        # if ['column7'] == IndexError:
        #     print('NA') 
        # item['column8'] = response.css('div.last::text').getall()[7].strip()
        # if ['column8'] == IndexError:
        #     print('NA')
        # item['column9'] = response.css('div.last::text').getall()[8].strip()  
        # if ['column9'] == IndexError:
        #     print('NA') 
        # item['column10'] = response.css('div.last::text').getall()[9].strip()  
        # if ['column10'] == IndexError:
        #     print('NA') 
        
        yield item
        
# if __name__ == "__main__":
#     p = CrawlerProcess()
#     p.crawl(LamudihouseSpider)
#     p.start()
