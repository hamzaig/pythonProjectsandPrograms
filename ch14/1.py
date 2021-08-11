def square(n):
    return n**2

s=square
print(square(3))
print(s(3))
print(s.__name__)
print(square.__name__)
print(s)
print(square)