a, b = [int(x) for x in input().split()]
c = int(input())
T = a * 60 + b + c
a = T // 60
b = T % 60
if a >= 24: # c 값이 하루 이상의 값(1440분 이상)이 입력되면 오류, 문제 조건에서 c는 1000 이하
    a -= 24
print(a, b)

# a, b = [int(x) for x in input().split()]
# c = int(input())
# T = a * 60 + b + c
# a = T // 60
# b = T % 60
# while a >= 24: # c 값에 상관없이 계산 가능
#     a -= 24
# print(a, b)