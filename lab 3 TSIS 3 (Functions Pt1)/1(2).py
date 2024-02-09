def n(arr)->list:
    k=False
    for i in range(len(arr)):
        if arr[i]==0 and arr[i+1]==0 and arr[i+2]==7:
            k=True
    return k
        

a = int(input())
arr = []
for i in range(a):
    i = int(input())
    arr.append(i)

result = n(arr)
print(result)