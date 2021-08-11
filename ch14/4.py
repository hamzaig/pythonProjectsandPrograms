def to_power(pow):
    def num(n):
        return n**pow
    return num
square = to_power(2)
print(square(3))