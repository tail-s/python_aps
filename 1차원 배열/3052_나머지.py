s = set()
for _ in range(10):
    x = int(input()) % 42
    s.add(x)
print(len(s))