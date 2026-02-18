data = [(1, 5), (2, 3), (4, 1)]

# 1
sorted_by_second = sorted(data, key=lambda x: x[1])

# 2
sorted_by_first = sorted(data, key=lambda x: x[0])

# 3
reverse_sort = sorted(data, key=lambda x: x[1], reverse=True)

# 4
numbers = [5, 2, 9, 1]
sorted_numbers = sorted(numbers, key=lambda x: -x)

print(sorted_by_second)
print(sorted_by_first)
print(reverse_sort)
print(sorted_numbers)
