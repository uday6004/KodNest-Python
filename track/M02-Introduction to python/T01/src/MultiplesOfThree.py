limit = int(input("Enter the limit: "))
target = int(input("Enter the target: "))

count = 0
total = 0
found = False

for i in range(1, limit + 1):
    if i % 3 == 0:
        total += i
        count += 1
        if i == target:
            found = True

print(count)
print(total)
if found:
    print("Found")
else:
    print("Not found")