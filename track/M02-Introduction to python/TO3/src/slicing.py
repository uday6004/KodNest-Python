word = input()

first = int(input("enter the first number:"))
second = int(input("enter the second number:"))
third = int(input("enter the third number:"))

numbers = [first, second, third]
record = (first, second, third)

# Perform slicing operations
sliced_word = word[1:-1]
sliced_list = numbers[:2]
reversed_tuple = record[::-1]

# Display outputs in the required format
print(f"Middle: {sliced_word}")
print(f"First Two: {sliced_list}")
print(f"Reversed Tuple: {reversed_tuple}")