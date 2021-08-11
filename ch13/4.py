numbers=[1,2,3,4,5,6]
squares=map(lambda i: i**2,numbers)

print(squares)

print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))
a=iter(numbers)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))


