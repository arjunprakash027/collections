from scrapy.crawler import CrawlerProcess
from bookscrapper.spiders.spider1 import Spider3Spider
from scrapy.utils.project import get_project_settings

process = CrawlerProcess(get_project_settings())
process.crawl(Spider3Spider,**{'-o':'out.json'})
process.start()