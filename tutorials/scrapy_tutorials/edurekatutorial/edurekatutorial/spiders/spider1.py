import scrapy 

class Quotes(scrapy.Spider):
    name = 'quotes'

    def start_request(self):
        urls = ['http://quotes.toscrape.com/page/1/','http://quotes.toscrape.com/page/2/']

        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)
    
    def parse(self,response):
        page = response.url.split("/")[-2]
        filename = 'quotes-{}.html'.format(page)

        with open(filename,'wb') as f:
            f.write(response.body)
        self.log("saved file {}".format(filename))


class Quotes2(scrapy.Spider):
    name = 'quotes2'
    start_urls = ['http://quotes.toscrape.com/page/1/','http://quotes.toscrape.com/page/2/']

    def parse(self,response):
        page = response.url.split("/")[-2]
        print('url split:')
        filename = "quotes{}.html".format(page)
        with open(filename,'wb') as f:
            f.write(response.body)

class Quotes3(scrapy.Spider):
    name = 'quotes3'
    start_urls = ['http://quotes.toscrape.com/page/1/','http://quotes.toscrape.com/page/2/']

    def parse(self,response):
        for quote in response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "author", " " ))]'):
            yield {'quote' : quote.extract()}

class Quotes4(scrapy.Spider):
    name = 'quotes4'
    start_urls = ['http://quotes.toscrape.com/page/1/','http://quotes.toscrape.com/page/2/']

    def parse(self,response):
        for quote in response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "quote", " " ))]'):
            yield {'quotes' : quote.css('span.text::text').get(),
                   'author' : quote.css('small.author::text').get()}
           
           





    