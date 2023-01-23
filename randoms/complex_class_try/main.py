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

class anotherclass:
    def __init__(self):
        pass

if __name__ == '__main__':
    for k in range(20):
        obj = MyClass(k,k+1)
        print("number:",obj.process_data()) 
        obj.counttotal()