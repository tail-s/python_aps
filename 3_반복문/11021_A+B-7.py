import sys
x = int(input())
for i in range(x):
    a, b = [int(x) for x in sys.stdin.readline().split()]
    print(f"Case #{i + 1}: {a + b }")