T = int(input())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = [int(x) for x in input().split()]
    dis = (((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** 0.5
    R = [r1, r2, dis]
    l = max(R); R.remove(l)
    s = min(R); R.remove(s)
    m = R[0]
    print(-1 if (dis == 0 and r1 == r2) else 1 if (dis == r1 + r2 or l == m + s) else 0 if (l > m + s) else 2)