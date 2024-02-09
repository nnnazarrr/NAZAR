def n(b):
    r = b[::-1]
    if r==b:
        return "palindrom"
    else:
        return "not palindrom"
    
    

b = str(input())
result = n(b)
print(result)