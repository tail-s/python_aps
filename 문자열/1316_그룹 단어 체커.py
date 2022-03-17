n = int(input())

ans = 0
for i in range(n):
    word = input()
    hist = []
    x = None

    for j in word:
        if x != j:
            if j in hist:
                break

            x = j
            hist.append(j)
    else:
        ans += 1

print(ans)