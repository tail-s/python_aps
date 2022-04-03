# import sys
#
# def isPrime(num):
#     if num == 1:
#         return False
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True
#
# def solve():
#     m, n = [int(x) for x in sys.stdin.readline().split()]
#     for i in range(m, n+1):
#         if isPrime(i):
#             print(i)
#
# solve()
# 소수의 정의를 이용

######################################################

# import math
# import sys
#
# def isPrime(num):
#     if num == 1:
#         return False
#     for i in range(2, int(math.sqrt(num)) + 1): # 소수의 특성을 이용
#         if num % i == 0:
#             return False
#     return True
#
# def solve():
#     m, n = [int(x) for x in sys.stdin.readline().split()]
#     for i in range(m, n+1):
#         if isPrime(i):
#             print(i)
#
# solve()

######################################################

import sys

def solve():
    m, n = [int(x) for x in sys.stdin.readline().split()]
    primes = [True] * (n + 1)
    primes[1] = False
    for i in range(2, n+1):
        if primes[i]:
            for j in range(i*2, n+1, i): # 합성수 찾기 (배수)
                primes[j] = False
    for i in range(m, n+1):
        if primes[i]:
            print(i)

solve()

# 에라토스테네스의 체가 뭔데







