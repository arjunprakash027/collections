import re
import requests
url = "https://quest.squadcast.tech/api/310620243005/worded_ip"
text = requests.get(url)
print(text.text)

def find_ip_address(passage):
    num_words = re.findall(r"\b(zero|one|two|three|four|five|six|seven|eight|nine)\b", passage)
    word_dict = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    num_ints = [word_dict[w] for w in num_words]
    
    print(len(num_ints))
    x = list(divide_chunks(num_ints, 10))
    for lis in x:
        lis.insert(3, '.')
        lis.insert(6, '.')
        lis.insert(9, '.')
        ip_address = ''.join(lis)
        print(ip_address)

        r = requests.post("https://quest.squadcast.tech/api/310620243005/submit/worded_ip", data={'answer': ip_address})
        print(r.text)

def divide_chunks(l, n):
     
    # looping till length l
    for i in range(0, len(l), n):
        yield l[i:i + n]
 
# How many elements each
# list should have

ip_address = find_ip_address(text.text)
if ip_address:
    print(ip_address)
else:
    print("No valid IP address found.")