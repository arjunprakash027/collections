# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BookscrapperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

def serialize_price(value): #serializer the data -> change its value while its being saved to database
    return f'{str(value)}'

class BookItem(scrapy.Item): #save data in database as feilds
    url = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field(serializer = serialize_price)
    type = scrapy.Field()
    aviliblity = scrapy.Field()
    rating = scrapy.Field()
    category = scrapy.Field()
    description = scrapy.Field()
