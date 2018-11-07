import scrapy

class Test(scrapy.Spider):
    name = 'xxx'
    start_urls = ['https://github.com/shiyanlou?tab=repositories']

    def parse(self, r):
        for i in r.xpath('//li[contains(@class, "col-12")]'):
            yield {
                'name': i.css('a::text').extract_first().strip(),
                'update_time': i.xpath('.//relative-time/@datetime').extract_first()
            }
        url = r.xpath('//div[@class="pagination"]/a')[-1].css('::attr(href)').extract_first()
        if r.xpath('//div[@class="pagination"]/a')[-1].css('::text').extract_first() == 'Next':
            yield r.follow(url, callback=self.parse)
