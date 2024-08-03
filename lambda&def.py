def x(n):
    return lambda a:a*n
y=x(2)
print(y(11))
#same as
y=lambda a,n:a*n
print(y(11,2))