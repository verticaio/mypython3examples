
static = [9, 8, 7, 6, 5]
baza = [1, 2, 3, 4, 5]
a = [i for i, j in zip(static, baza) if i > j]
if len(a) > 0:
    print(a)
    for i in a:
        baza.append(i)
print(baza)