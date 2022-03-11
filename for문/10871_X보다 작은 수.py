import sys
N, X = map(int, sys.stdin.readline().split())
A = [int(x) for x in sys.stdin.readline().split()]
for item in A:
    if item < X:
        print(item, end=" ")