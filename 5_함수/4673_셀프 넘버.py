def d(n):
    i_sum = 0
    total = 0
    for i in str(n):
        i_sum += int(i)
    total = n + i_sum
    return total

arr = []
arr_d = []
for i in range(1, 10001):
    arr.append(i)
    arr_d.append(d(i))

for i in range(10000):
    if arr_d[i] in arr:
        arr.remove(arr_d[i])

num = len(arr)
for i in range(num):
    print(arr[i])