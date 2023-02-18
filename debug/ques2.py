class read:
    def read_file(self, file_name):
        with open(file_name, 'r') as f:
            return f.read()

def main():
    r = read()
    print(r.read_file('test.txt'))

main()