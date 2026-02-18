# 1
def sum_all(*args):
    return sum(args)

# 2
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

# 3
def mix(a, *args):
    print("First:", a)
    print("Others:", args)

# 4
def full_info(name, **kwargs):
    print("Name:", name)
    print("Details:", kwargs)

print(sum_all(1, 2, 3, 4))
print_info(name="Bekzat", age=18)
mix(10, 20, 30)
full_info("Ali", age=18, city="Almaty")
