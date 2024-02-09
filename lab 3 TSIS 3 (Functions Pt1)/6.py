def n(arr)->list:
    k=False
    for i in range(len(arr)):
        if arr[i]==3 and arr[i+1]==3:
            k=True
    return k
        

a = int(input())
arr = []
for i in range(a):
    i = int(input())
    arr.append(i)

result = n(arr)
print(result)