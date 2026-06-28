import scrapy


class LittlegamesSpider(scrapy.Spider):
    name = "littlegames"
    allowed_domains = ["4399.com"]
    start_urls = ["https://4399.com"]

    def parse(self, response):
    # def parse(self, response,**kwargs):
        list = response.xpath('//ul[@class="tm_list "]/li')
        for li in list:
            name = li.xpath('./a/img/@alt').extract_first()
            p = {
                'name':name
            }
            yield p
        name1 = response.xpath('//ul[@class="tm_list"]/li/a/img/@alt').extract()
        name2 = response.xpath('//ul[@class="tm_list lf_ul"]/li/a/img/@alt').extract()
        name3 = response.xpath('//ul[@class="tm_list g-ul cf"]/li/a/img/@alt').extract()
        name4 = response.xpath('//ul[@class="tm_list o-ul list-item"]/li/a/img/@alt').extract()


