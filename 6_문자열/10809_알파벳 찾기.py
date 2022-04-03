s = input()
arr = [-1] * 26
for i in range(len(s)):
    x = s[i]
    o = ord(x) - 97
    if arr[o] == -1:
        arr[o] = i
print(' '.join(map(str, arr)))