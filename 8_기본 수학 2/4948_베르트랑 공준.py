# is_on = True
# while is_on:
#     n = int(input())
#     if n == 0:
#         is_on = False
#     else:
#         arr = []
#         for i in range(n + 1, (n * 2) + 1):
#             err = 0
#             if i > 1:
#                 for j in range(2, i): # 2부터 i-1까지
#                     if i % j == 0:
#                         err += 1
#                         break # 2부터 i-1까지 나눈 몫이 0이면 err가 증가하고 break
#                 if err == 0:
#                     arr.append(i) # err가 없으면 소수를 리스트에 추가
#         print(len(arr)) 시간초과 뭐냐고!

########################################################
# 이건 왜안됨?

# def solve():
#     is_on = True
#     while is_on:
#         x = int(input())
#         if x == 0:
#             is_on = False
#             pass
#         elif x == 1:
#             print("1")
#         else:
#             m = x + 1
#             n = m * 2
#             primes = [True] * (n + 1)
#             primes[0] = False
#             cnt = 0
#             for i in range(2, n+1):
#                 if primes[i]:
#                     for j in range(i*2, n+1, i): # 합성수 찾기 (배수)
#                         primes[j] = False
#             for i in range(m, n+1):
#                 if primes[i]:
#                     # print(i)
#                     cnt += 1
#             print(cnt)
# solve()
# 풀이중 - 실패함 whY?

########################################################

# def sosu(x):
#     if x == 1:
#         return False
#     for i in range(2, int(x ** 0.5) + 1):
#         if x % i == 0: # 제곱근이 있는 수 중 약수가 있으면 소수 아님
#             return False
#     return True # 나머지는 다 소수
#
# while True:
#     n = int(input())
#     cnt = 0
#     if n == 0:
#         break
#     for i in range(n + 1, (2 * n) + 1):
#         if sosu(i):
#             cnt += 1
#     print(cnt)

# 응 시간제한이야~ 다시해와~
########################################################

def sosu(x):
    if x == 1:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0: # 제곱근이 있는 수 중 약수가 있으면 소수 아님
            return False
    return True # 나머지는 다 소수

arr = list(range(2, 246912)) # 문제 조건으로 제한
test = []

for i in arr:
    if sosu(i):
        test.append(i)

import sys

while True:
    n = int(sys.stdin.readline())
    cnt = 0
    if n == 0:
        break
    for i in test:
        if n < i <= 2 * n:
            cnt += 1
    print(cnt)