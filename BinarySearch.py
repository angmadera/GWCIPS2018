num = []

int(input("How many elements do you want in your list?"))
max = int(input())

for i in range(max):
    num.append(random.randrange(1, 101, 1))
    num.sort()
    
