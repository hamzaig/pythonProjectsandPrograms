def is_even(a):
    return a%2==0
numbers=[1,2,3,4,5,6,7,8,9,10]

a=filter(is_even,numbers)
b=list(filter(is_even,numbers))
c=tuple(filter(is_even,numbers))
d=tuple(filter(lambda a: a%2==0,numbers))
print(a)
for i in a:
    print(i)
for i in a:
    print(i)
print(b)
print(c)
print(d)
for i in b:
    print(i)
for i in b:
    print(i)


new_list=[i for i in numbers if i%2==0 ]
print(new_list)