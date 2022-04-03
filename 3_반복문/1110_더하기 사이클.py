x = y = int(input())
count = 0

while True:
    a = x // 10 # 10의 자리 수
    b = x % 10 # 1의 자리 수
    c = a + b
    count += 1
    x = (b * 10) + (c % 10)
    if x == y:
        break
print(count)