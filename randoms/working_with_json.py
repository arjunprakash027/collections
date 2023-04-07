import json 
import jmespath
import csv

details = {'details': [
    {
    'name': 'John',
    'age': 30,
    'married': True,
    'divorced': False,
    'children': ('Ann','Billy'),
    'pets': None,
    'cars': [{'model': 'BMW 230', 'mpg': 27.5},
             {'model': 'Ford Edge', 'mpg': 24.1},]
},
    {
    'name': 'rajesh',
    'age': 30,
    'married': True,
    'divorced': False,
    'children': ('kumaresh','murugesh'),
    'pets': None,
    'cars': [{'model': 'BMW 230', 'mpg': 27.5},
                {'model': 'Ford Edge', 'mpg': 24.1},]
},
]}

with open('sample.json','w') as outfile:
    json.dump(details,outfile,indent=4)

with open('sample.json', 'r') as infile:
    data = json.load(infile)

#print(data)

print(jmespath.search("details[*].name",data))

print(data['details'])

new_entry = {
    'name': 'kumaresh',
    'age': 30,
    'married': True,
    'divorced': False,
    'children': ('kumaresh','murugesh'),
    'pets': None,
    'cars': [{'model': 'BMW 230', 'mpg': 27.5},
                {'model': 'Ford Edge', 'mpg': 24.1},]
}

with open('sample.json','r+') as editfile:
    file_data = json.load(editfile)
    file_data['details'].append(new_entry)
    editfile.seek(0)
    json.dump(file_data,editfile,indent=4)

print(file_data['details'])


#writing to a csv file
data_file = open('sample.csv', 'w')
csv_writer = csv.writer(data_file)

count = 0
for val in file_data['details']:
    if count == 0:
        header = val.keys()
        csv_writer.writerow(header)
        count += 1
    csv_writer.writerow(val.values())
data_file.close()







