# import sys
#
# pts = []
# x = y = 0
# for _ in range(3):
#     pt = [int(x) for x in sys.stdin.readline().split()]
#     pts.append(pt)
#
# if pts[0][0] == pts[1][0]:
#     x = pts[2][0]
# elif pts[1][0] == pts[2][0]:
#     x = pts[0][0]
# else:
#     x = pts[1][0]
#
# if pts[0][1] == pts[1][1]:
#     y = pts[2][1]
# elif pts[1][1] == pts[2][1]:
#     y = pts[0][1]
# else:
#     y = pts[1][1]
#
# print(f"{x} {y}")

x = []
y = []

for _ in range(3):
    a, b = map(int, input().split())

    if a in x:
        x.remove(a)
    else:
        x.append(a)
    if b in y:
        y.remove(b)
    else:
        y.append(b)

print(*x, *y)



