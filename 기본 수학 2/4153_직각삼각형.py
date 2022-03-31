
is_on = True
while is_on:
    arr = [int(x) for x in input().split()]
    if arr == [0, 0, 0]:
        is_on = False
        break

    arr.sort()
    a = arr[0]
    b = arr[1]
    c = arr[2]
    if (c ** 2) == (b ** 2) + (a ** 2):
        print("right")
    else:
        print("wrong")
