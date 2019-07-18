from ..items import CrawlerItem
import scrapy
import logging

host_domain = 'https://nba.udn.com'

class NbaSpider(scrapy.Spider):
    name = 'nba'
    allowed_domains = ['nba.udn.com']
    start_url = ['https://nba.udn.com/nba/cate/6754/-1/newest/1']

    def parse(self, response):
        targets = response.xpath('//*[@id="news_list_body"]/dl/dt')

        for target in targets:
            url = host_domain + target.xpath('a/@href').get()
            yield scrapy.Request(url, callback=self.parse_article)

    def parse_article(self, response):
        item = CrawlerItem()
        try:
            item['title'] = response.xpath('//*[@id="story_body_content"]/h1/text()').get()
            item['author_time'] = response.xpath('//*[@id="shareBar"]/div[2]/div/span/text()').get()
            item['image_source'] = response.xpath('//*[@id="story_body_content"]/span/figure/a/img/@src').get()
            item['video_source'] = response.xpath('//*[@id="player"]/div/video/@src').get()
            content = response.xpath('').getall()           
            for text in content:
                if text is not None:
                    item['content'] += text
            yield item
        except Exception as e:
            logging.error(str(e))