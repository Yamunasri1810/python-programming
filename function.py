a = [10, 20, 30, 40]
b = list(filter(lambda a:a>15, a))
print(b)

x = lambda y,z:y+z
print(x(10 ,15))

print(*a)
print(*b)

def abc(*x):
    print(x[0], " ", x[1])
abc(10, 15)

def abc(**x):
    print(x['b'])
abc(a=10, b=29, c=12,d=19)