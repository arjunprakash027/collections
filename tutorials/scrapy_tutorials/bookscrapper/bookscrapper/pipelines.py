# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class BookscrapperPipeline:

    def process_item(self, item, spider):

        print("pipeline item ____________>",item)
        adapter = ItemAdapter(item)
        print("pipeline adapter ____________>",adapter)

        #strips all the whitespaces from everything excpet description
        field_names = adapter.field_names()
        print("field names ____________>",field_names)
        for field_name in field_names:
            if field_name != 'description':
                value = adapter.get(field_name)
                print("-------------------------->",value)
                adapter[field_name] = value[0].strip()

        
        #converts all uppercase into lowercase
        lowercase_keys = ['category','type']
        for lowercase_key in lowercase_keys:
            value = adapter.get(lowercase_key)
            adapter[lowercase_key] = value.lower()
        
        #converts price to float
        price_string = adapter.get('price')
        price_string = price_string.split('£')[1]
        print("scrapped price string __________>",price_string)
        adapter['price'] = float(price_string)

        #gets only number from aviliblity
        aviliblity_string = adapter.get('aviliblity')
        split_string_array = aviliblity_string.split('(')
        if len(split_string_array) < 2:
            adapter['aviliblity'] = 0
        else:
            avi_array = split_string_array[1].split(' ')
            adapter['aviliblity'] = int(avi_array[0])
        

        return item

#import mysql.connector
class Savetomysqlpipeline:
    
    def __init__(self):
        self.conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'password',
            database = 'books',
            port  = 5000
        )
        self.curr = self.conn.cursor()

        self.curr.execute(""" 
        CREATE TABLE if not exists books (
            id int not null auto_increment,
            url varchar(255),
            title TEXT,
            price DECIMAL,
            type varchar(255),
            aviliblity int,
            rating varchar(255),
            category varchar(255),
            description TEXT,
            primary key (id));
            """)

    def process_item(self, item, spider):
        print("this is the item:::::",item)

        self.curr.execute("""insert into books(url,title,price,type,aviliblity,rating,category,description) values(%s,%s,%s,%s,%s,%s,%s,%s)""",(
            item['url'],
            item['title'],
            item['price'],
            item['type'],
            item['aviliblity'],
            item['rating'],
            item['category'],
            item['description']
        ))
        self.conn.commit()
        return item
    
    def close_spider(self,spider):

        self.curr.close()
        self.conn.close()