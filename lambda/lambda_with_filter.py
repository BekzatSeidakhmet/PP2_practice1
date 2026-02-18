numbers = [1, 2, 3, 4, 5, 6]

# 1
evens = list(filter(lambda x: x % 2 == 0, numbers))

# 2
odds = list(filter(lambda x: x % 2 != 0, numbers))

# 3
greater_than_three = list(filter(lambda x: x > 3, numbers))

# 4
small_numbers = list(filter(lambda x: x < 4, numbers))

print(evens)
print(odds)
print(greater_than_three)
print(small_numbers)
