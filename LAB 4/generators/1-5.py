#exercise 1
def square_(n):
    for i in range(1, n + 1):
        yield i ** 2

n = int(input())
for squared_n in square_(n):
    print(squared_n)

#exercise 2
def even_n(n):
    for i in range(2, n + 1, 2):
        yield i
    
n = int(input())
even_gen = even_n(n)
print(','.join(map(str, even_gen)))

#exercise 3
def func(n):
    for i in range(n + 1):
        if i%3==0 and i%4==0:
            yield i

n = int(input())
for num in func(n):
    print(num)

#exercise 4
def squares(a, b):
    for i in range(a, b + 1):
        yield i**2

a = int(input())
b = int(input())
for s_num in squares(a, b):
    print(s_num)

#exercise 5
def func(n):
    while n >= 0:
        yield n
        n -= 1

n = int(input())
for num in func(n):
    print(num)