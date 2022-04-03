n = int(input())
f = 2
pf = []
while n >= f:
    if n % f == 0:
        pf.append(f)
        n = n / f
    else:
        f = f + 1
for i in pf:
    print(i)