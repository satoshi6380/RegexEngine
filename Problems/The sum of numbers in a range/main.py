def range_sum(numbers, start, end):
    return sum(int(n) for n in numbers if int(start) <= int(n) <= int(end))


input_numbers = input().split()
a, b = input().split()
print(range_sum(input_numbers, a, b))
