import math

#1
def radian(n):
    a = (n * math.pi)/180
    yield round(a, 6)

n = int(input())
for s in radian(n):
    print(s)

#2
def area(H, f, s):
    a = 0.5*(f+s)*H
    yield a

H = int(input())
f = int(input())
s = int(input())
for s in area(H, f, s):
    print(s)

#3
def area(sides, length):
    area = (sides * length ** 2) / (4 * math.tan(math.pi / sides))
    yield area

sides = int(input())
length = float(input())
for s in area(sides, length):
    print(s)

#4
def area(a, h):
    area = a*h
    yield area

a = float(input())
h = float(input())
for s in area(a, h):
    print(s)