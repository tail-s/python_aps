import sys

# a, b = map(int, sys.stdin.readline().split())
# a, b = [int(x) for x in sys.stdin.readline().split()]
# data = list(map(int, sys.stdin.readline().split()))

# x = int(input())
# for _ in range(x):
#     a, b = map(int, sys.stdin.readline().split())
#     print(a + b)

# x = int(input())
# for _ in range(x):
#     a, b = [int(x) for x in sys.stdin.readline().split()]
#     print(a + b)

data = []
x = int(input())
for i in range(x):
    data.append(list(map(int, sys.stdin.readline().split())))
    print(data[i][0] + data[i][1])

