x = int(input())
y = input()
z = int(len(y))
total = 0

for i in range(z):
    total += int(y[i])

print(total)