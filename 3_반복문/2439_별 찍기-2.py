# x = int(input())
# for i in range(1, x+1):
#     print(" " * (x - i), end='')
#     print("*" * i, end='')
#     print("")
# 위 3줄 대신 print(" " * (N - i), "*" * i, sep="")

n = int(input())
for i in range(1, n+1):
    for _ in range(n-i):
        print(" ", end="")
    for _ in range(i):
        print("*", end="")
    print("")