m = int(input())
n = int(input())

arr = []
for i in range(m, n + 1):
    err = 0
    if i > 1:
        for j in range(2, i): # 2부터 i-1까지
            if i % j == 0:
                err += 1
                break # 2부터 i-1까지 나눈 몫이 0이면 err가 증가하고 break
        if err == 0:
            arr.append(i) # err가 없으면 소수를 리스트에 추가

if len(arr) > 0:
    print(sum(arr))
    print(min(arr))
else:
    print("-1")