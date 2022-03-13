def solve(n):
    if n < 100:
        return True

    tmp = str(n)
    for i in range(len(tmp) - 2):
        if int(tmp[i]) + int(tmp[i + 2]) != 2 * int(tmp[i + 1]):
            return False

    return True

x = int(input())

cnt = 0
for i in range(1, x + 1):
    if solve(i):
        cnt += 1

print(cnt)