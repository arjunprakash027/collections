import requests

class MyClass(object):
    count = 0
    def __init__(self,input_data,input_data2):
        self.data = input_data
        self.data2 = input_data2
        MyClass.count += 1

    def process_data(self):
        # process the input data and return the result
        result = self.data + self.data2
        return result

    def counttotal(self):
        print('count:',MyClass.count)

class CricketScore:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_score(self, match_id):
        url = f"http://cricket-api.com/api/cricketScore?apikey={self.api_key}&unique_id={match_id}"
        response = requests.get(url)
        return response.json()

    def print_score(self, match_id):
        score = self.get_score(match_id)
        print(f"Score for match {match_id} is:")
        print(f"Team 1: {score['team-1']}")
        print(f"Team 2: {score['team-2']}")
        print(f"Current Score: {score['score']}")

if __name__ == '__main__':
    for k in range(20):
        obj = MyClass(k,k+1)
        print("number:",obj.process_data()) 
        obj.counttotal()