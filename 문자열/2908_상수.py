x = input().split()
for i in range(2):
    x[i] = x[i][2] + x[i][1] + x[i][0]
print(max(x))

# import sys
#
# a, b = map(str,sys.stdin.readline().split())
# a = list(a)
# a.reverse()
#
# b = list(b)
# b.reverse()
# print(max(int(''.join(a)),int(''.join(b))))