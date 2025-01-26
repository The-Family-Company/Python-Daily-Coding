def get_smaller_numbers (numbers, n):
    smaller_numbers = []
    for number in numbers:
        if number < n:
            smaller_numbers.append(number)
    return smaller_numbers

numbers_list = [10, 25, 8, 15, 3, 40, 21, 26, 23, 100]
n = 55
result = get_smaller_numbers(numbers_list, n)
print("Smaller Numbers:",n,result)