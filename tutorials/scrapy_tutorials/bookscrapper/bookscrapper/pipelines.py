# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class BookscrapperPipeline:

    def process_item(self, item, spider):

        adapter = ItemAdapter(item)

        #strips all the whitespaces from everything excpet description
        field_names = adapter.field_names()
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
