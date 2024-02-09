def n(arr):
    rr = []
    
    for i in arr:
        k=True
        for g in range(2, i):
            if i%g==0:
                k=False
        if k: 
            rr.append(i)
    return rr
            

a = int(input())
arr = []
for i in range(a):
    i = int(input())
    arr.append(i)

print(n(arr))