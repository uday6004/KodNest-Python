word =input("Enter String:")

first = int(input("Enter first Number:"))
second = int(input("Enter Sencond Number:"))
third = int(input("Enter Third Number:"))

number = [first, second, third]
record = (first, second, third)

slice_word = word[1:-1]
slice_list = number[:2]
reversed_tuple = record[-1:]

print(f"Slice Word: {slice_word}")
print(f"Slice List: {slice_list}")
print(f"Reversed Tuple: {reversed_tuple}")