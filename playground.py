def make_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

my_counter = make_counter()
print(my_counter())  # Output: 1
print(my_counter())  # Output: 2
