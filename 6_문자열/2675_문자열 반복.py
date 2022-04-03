# t = int(input())
# result = []
# for i in range(t):
#     arr = [x for x in input().split()]
#     r = int(arr.pop(0))
#     p = arr[0]
#     n = len(p)
#     for j in range(n):
#         result.append(p[j]*r)
#     print(''.join(result))
#     result.clear()

n = int(input())

for _ in range(n):
    num, text = input().split()
    t = ''
    for i in text:
        t += i*int(num)
    print(t)