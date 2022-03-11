import sys
x = int(input())
for i in range(x):
    a, b = map(int, sys.stdin.readline().split())
    print(f"Case #{i + 1}: {a} + {b} = {a + b }")