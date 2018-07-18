numbers = []
numInput1 = int(input("Give me a number. "))
numInput2 = int(input("Give me another number. "))
numInput3 = int(input("Give me another number. "))
numInput4 = int(input("Give me another number. "))
numInput5 = int(input("Give me another number. "))

numbers.append(numInput1)
numbers.append(numInput2)
numbers.append(numInput3)
numbers.append(numInput4)
numbers.append(numInput5)

print("The list of items are {}".format(numbers))

x = int(input("Enter item to search: "))

i = flag = 0

while i < len(numbers):
    if numbers[i] == x:
        flag = 1
        break

    i = i + 1

if flag == 1:
    print("item found at position:", i)
else:
    print("item not found")
