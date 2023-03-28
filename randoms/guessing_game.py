import random
a = random.randint(1, 50)
count = 0
while True:
    num = int(input("your guess between 1 to 50 \n"))
    count += 1
    print("try number {}".format(count))
    if num == a:
        print("your guess was right")
        print("number of try was {}".format(count))
        break

    elif num < a:
        print("-----------------------------")
        print("your guess is lesser than actual number")
        print("-----------------------------")

    elif num > a:
        print("-----------------------------")
        print("your guess is greater than actual number")
        print("-----------------------------")
