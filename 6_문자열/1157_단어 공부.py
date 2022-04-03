text = input().upper()
hist = {}

for i in text:
    if i in hist.keys():
        hist[i] += 1
    else:
        hist[i] = 1

big = 0
for key in hist.keys():
    big = max(big, hist[key])

cnt = 0
for key in hist.keys():
    if hist[key] == big:
        cnt += 1
        result = key
if cnt != 1:
    print("?")
else:
    print(result)