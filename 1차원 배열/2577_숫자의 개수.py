arr = []
x = 1
cnt = [0] * 10
for i in range(3):
    arr.append(int(input()))
    x *= arr[i]
while x != 0:
    cnt[x % 10] += 1
    x //= 10
for item in cnt:
    print(item)