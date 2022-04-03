def Goldbach():
    arr = [False, False] + [True] * 10000

    for i in range(2, 101): # 10000 의 루트값까지만 걸러도 ok니까
        if arr[i] == True:
            for j in range(i + i, 10001, i):
                arr[j] = False

    t = int(input())
    for _ in range(t):
        n = int(input())
        a = n // 2
        b = a
        for _ in range(10000):
            if arr[a] and arr[b]:
                print(a, b)
                break
            a -= 1
            b += 1 # 소수가 아니면 하나씩 벌리면 됨

Goldbach()