n = int(input())
a = list(map(int, input().split()))

def solve(n): # n 까지의 모든 소수를 구하는 함수
    arr = [True] * (n + 1) # 0부터 n까지
    arr[0] = arr[1] = False
    x = int(n ** 0.5)

    for i in range(2, x + 1):
        if arr[i]:
            for j in range(i * i, n + 1, i):
                arr[j] = False
    return arr

b = solve(1000)
rst = 0

for i in a:
    if b[i]:
        rst += 1

print(rst)