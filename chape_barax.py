numbers =[]
while True:
    n = int(input())
    if n == 0:
        break
    numbers.append(n)
for i in range(len(numbers), 0, -1):
    print(numbers[i-1])
    