arr = []
for _ in range(9):
    arr.append(int(input()))

big = 0
for i in range(9):
    if arr[i] > big:
        big = arr[i]
        idx = i
print(big, idx + 1, sep="\n")