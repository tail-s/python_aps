n = int(input())

for _ in range(n):
    h, w, n = map(int, input().split())

    flo = n % h
    num = n // h + 1

    if flo == 0:
        num = n // h
        flo = h

    print(f"{flo * 100 + num}")
