from gazeta.items import GazetaItem
import scrapy
from urllib.parse import urljoin


# scrapy crawl gazeta -o output.json

class GazetaSpider(scrapy.Spider):
    name = "gazeta"
    start_urls = ['https://www.gazeta.ru/news/']
    visited_urls = []

    def parse_post(self, response):
        item = GazetaItem()
        title = response.xpath('//*[@id="news-content"]/article/h1/text()').extract()
        item['title'] = title
        body = response.xpath('//div[@itemprop="articleBody"]//p//text()').extract()
        item['body'] = body
        date = response.xpath('//*[@id="news-content"]/article/div[1]/time/text()').extract()
        item['date'] = date
        url = response.url
        item['url'] = url
        yield item

    def parse(self, response):
        if response.url not in self.visited_urls:
            self.visited_urls.append(response.url)
            for post_link in response.xpath('//a[@itemprop="mainEntityOfPage url"]/@href').extract():
                url = urljoin(response.url, post_link)
                yield response.follow(url, callback=self.parse_post)

            next_pages = response.xpath('//li[contains(@class, "page-item") and'
                                        ' not(contains(@class, "active"))]/a/@href').extract()
            next_page = next_pages[-1]

            next_page_url = urljoin(response.url + '/', next_page)
            yield response.follow(next_page_url, callback=self.parse)
