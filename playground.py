def multiplier(factor):
    def inner_function(number):
        return number * factor
    return inner_function




# Create multiplier functions using the factory function
double = multiplier(2)
triple = multiplier(3)

# Use the generated functions
print(double(5))  # Output: 10
print(triple(5))  # Output: 15





# Define an empty set
empty_set = set()

# For loop over the empty set
for element in empty_set:
    print(element)

# This loop body will not execute because the set is empty
print("Loop completed")

# Define an empty list
empty_list = []

# For loop over the empty list
for element in empty_list:
    print(element)
    print("hello")

# This loop body will not execute because the list is empty
print("Loop completed")
