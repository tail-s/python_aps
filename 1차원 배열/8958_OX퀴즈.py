n = int(input())
for i in range(n):
    x = input()
    score = 0
    bonus = 0
    for j in x:
        if j == "O":
            bonus += 1
            score += bonus
        else:
            bonus = 0
    print(score)