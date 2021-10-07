def lonelyinteger(a):
    for i in range(0, len(a) - 1):
        candidate = a[i]
        for j in range(i + 1, len(a)):
            if a[j] == candidate:
                break
            if j == len(a) - 1 and candidate != a[j]:
                return candidate
