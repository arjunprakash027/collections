import scrapy
from bookscrapper.items import BookItem
import random

class Spider1Spider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com"] #when crawling multiple domains, it lists domains only we want to scrap
    start_urls = ["http://books.toscrape.com/"]

    def parse(self, response): # diffent peice of information we need to get extracted
        books = response.css('article.product_pod')

        for book in books:
            yield {
                'name' : book.css('h3 a').attrib['title'],
                'price' : book.css('div.product_price p.price_color::text').get(),
                'link' : book.css('h3 a').attrib['href']
            }
        
        next_page = response.css('li.next a::attr(href)').get() #get the next button link in the end of the page to navigate to the next page

        if next_page is not None: #recursively use the parse until there is no next button
            if 'catalogue/' in next_page:
                next_page_url = self.start_urls[0] + next_page
            else:
                next_page_url = self.start_urls[0] + "catalogue/" + next_page
            yield response.follow(next_page_url, callback = self.parse)


class Spider2Spider(scrapy.Spider):
    name = "indibook"
    allowed_domains = ["books.toscrape.com"] #when crawling multiple domains, it lists domains only we want to scrap
    start_urls = ["http://books.toscrape.com/"]

    def parse(self, response): # diffent peice of information we need to get extracted
        books = response.css('article.product_pod')

        for book in books:
            book_details = book.css('h3 a ::attr(href)').get()

            if 'catalogue/' in book_details:
                book_details_url = self.start_urls[0] + book_details
            else:
                book_details_url = self.start_urls[0] + "catalogue/" + book_details

            yield response.follow(book_details_url, callback=self.parse_book_page)
        
        next_page = response.css('li.next a::attr(href)').get() #get the next button link in the end of the page to navigate to the next page

        if next_page is not None: #recursively use the parse until there is no next button
            if 'catalogue/' in next_page:
                next_page_url = 'http://books.toscrape.com/' + next_page
            else:
                next_page_url = 'http://books.toscrape.com/' + "catalogue/" + next_page
            yield response.follow(next_page_url, callback = self.parse)
    
    def parse_book_page(self,response):
        table_rows = response.css("table tr")

        yield {
            'url' : response.url,
            'title' : response.css('div.product_main h1::text').get(),
            'price' : response.css('p.price_color ::text').get(),
            'type' : table_rows[1].css("td ::text").get(),
            'aviliblity' : table_rows[5].css("td ::text").get(),
            'rating' : response.css('p.star-rating').attrib['class'][11:],
            'category' : response.xpath("//ul[@class='breadcrumb']/li[@class='active']/preceding-sibling::li[1]/a/text()").get(),
            'description' : response.xpath("//div[@id='product_description']/following-sibling::p/text()").get()
        }

class Spider3Spider(scrapy.Spider):
    name = "indibook2"
    allowed_domains = ["books.toscrape.com"] #when crawling multiple domains, it lists domains only we want to scrap
    start_urls = ["http://books.toscrape.com/"]

    # custom_settings = {
    #     'FEED_FORMAT' : 'json',
    #     'FEED_URI' : 'out.json'
    # }

    # user_agent_list = [
    #     'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/83.0.4103.61 Chrome/83.0.4103.61 Safari/537.36',
    #     'Mozilla/5.0 (X11; Linux i686; rv:77.0) Gecko/20100101 Firefox/77.0',
    #     'Mozila/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)',
    #     'Mozilla5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/77.0',
    # ]

    def parse(self, response): # diffent peice of information we need to get extracted
        books = response.css('article.product_pod')

        for book in books:
            book_details = book.css('h3 a ::attr(href)').get()

            if 'catalogue/' in book_details:
                book_details_url = self.start_urls[0] + book_details
            else:
                book_details_url = self.start_urls[0] + "catalogue/" + book_details

            yield response.follow(book_details_url, callback=self.parse_book_page)
        
        next_page = response.css('li.next a::attr(href)').get() #get the next button link in the end of the page to navigate to the next page

        if next_page is not None: #recursively use the parse until there is no next button
            if 'catalogue/' in next_page:
                next_page_url = 'http://books.toscrape.com/' + next_page
            else:
                next_page_url = 'http://books.toscrape.com/' + "catalogue/" + next_page
            yield response.follow(next_page_url, callback = self.parse)
    
    def parse_book_page(self,response):
        table_rows = response.css("table tr")

        book_item = BookItem()
        book_item['url'] = response.url,
        book_item['title'] = response.css('div.product_main h1::text').get(),
        book_item['price'] = response.css('p.price_color ::text').get(),
        book_item['type'] = table_rows[1].css("td ::text").get(),
        book_item['aviliblity'] = table_rows[5].css("td ::text").get(),
        book_item['rating'] = response.css('p.star-rating').attrib['class'][11:],
        book_item['category'] = response.xpath("//ul[@class='breadcrumb']/li[@class='active']/preceding-sibling::li[1]/a/text()").get(),
        book_item['description'] = response.xpath("//div[@id='product_description']/following-sibling::p/text()").get()
        
        yield book_item # this final yeild that gives the dataitem is used in pipeline. 