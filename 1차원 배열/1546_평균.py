import sys
n = int(input())
arr = [int(x) for x in sys.stdin.readline().split()]
re = []

for i in range(n):
    re.append((arr[i]/max(arr))*100)

print(sum(re) / n)