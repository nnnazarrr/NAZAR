def unique(a):
    list = []
    for i in a:
        if i not in list:
            list.append(i)
    return list

b = int(input())
c = []
for i in range(b):
    i = str(input())
    c.append(i)
result = unique(c)
print(result)