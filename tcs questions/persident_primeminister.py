def question():
    """
    There are n numbers in international conference and prime minister and president of india must sit togather, find number of combination
    that can do that 
    """
    pass
n = int(input("number of members:"))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(f"total number of ways they can sit is {factorial(n-1)*(2)}")