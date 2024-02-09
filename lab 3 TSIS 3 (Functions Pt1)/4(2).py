def n(arr):
    for i in arr:
        for j in range(i):
            print("*",end="")
        print(end=" ")
        
    
a = int(input())
arr = []
for i in range(a):
    i = int(input())
    arr.append(i)
n(arr)