n = int(input())
for _ in range(n):
    arr = [int(x) for x in input().split()]
    num = arr.pop(0)
    avg = sum(arr[:])/num
    cnt = 0

    for i in range(num):
        if avg < arr[i]:
            cnt += 1
    per = (cnt/num)*100
    print(f"{per:.3f}%")