def find_largest_sum(numbers, num_digits):
    if not isinstance(numbers, list):
        raise TypeError("numbers must be a list")
    if not all(isinstance(i, int) for i in numbers):
        raise TypeError("all elements in numbers must be integers")
    if not isinstance(num_digits, int):
        raise TypeError("num_digits must be an integer")
    if len(numbers) < num_digits:
        raise ValueError("num_digits must be less than or equal to the length of numbers")
    max_sum = 0
    for i in range(len(numbers) - num_digits + 1):
        curr_sum = 0
        for j in range(i, i + num_digits):
            curr_sum += numbers[j]
        if curr_sum > max_sum:
            max_sum = curr_sum
    return max_sum

def find_largest_product(numbers, num_digits):
    if not isinstance(numbers, list):
        raise TypeError("numbers must be a list")
    if not all(isinstance(i, int) for i in numbers):
        raise TypeError("all elements in numbers must be integers")
    if not isinstance(num_digits, int):
        raise TypeError("num_digits must be an integer")
    if len(numbers) < num_digits:
        raise ValueError("num_digits must be less than or equal to the length of numbers")
    max_product = 0
    for i in range(len(numbers) - num_digits + 1):
        curr_product = 1
        for j in range(i, i + num_digits):
            curr_product *= numbers[j]
        if curr_product > max_product:
            max_product = curr_product
    return max_product

def compare_sums_and_products(numbers, num_digits):
    largest_sum = find_largest_sum(numbers, num_digits)
    largest_product = find_largest_product(numbers, num_digits)
    if largest_sum > largest_product:
        return "sum"
    elif largest_sum < largest_product:
        return "product"
    else:
        return "same"

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
num_digits = 4
print(compare_sums_and_products(numbers, num_digits))
