number = int(input("enter number"))
rep = int(input("enter digits"))

def digitvalue(n):
    digit_sum = 0
    temp = n
    while temp>0:
        digit_val = temp%10
        digit_sum += digit_val
        temp = temp//10
    return digit_sum

total_sum = 0
total_sum += digitvalue(number) * rep

while total_sum//10 != 0:
    total_sum = digitvalue(total_sum)
print(total_sum)
