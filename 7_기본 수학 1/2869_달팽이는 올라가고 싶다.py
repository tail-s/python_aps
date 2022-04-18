# A, B, V = map(int, input().split())
# cnt = 0
#
# while V > 0:
#     V -= A
#     if V > 0:
#         V += B
#     cnt += 1
#
# print(cnt)

# a, b, v = map(int, input().split())
# day = 0
# height = 0
#
# while True:
#     day += 1
#     height += a
#     if height >= v:
#         print(day)
#         break
#     height -= b

import sys, math

A, B, V = map(int, sys.stdin.readline().split())
day = (V - B) / (A - B)
print(math.ceil(day))