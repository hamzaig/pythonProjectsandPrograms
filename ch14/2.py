# def square(a):
#     return a**2
# l=[1,2,3,4]
# print(list(map(square,l)))

# def square(a):
#     return a**2
# l=[1,2,3,4]
# print(list(map(lambda a: a**2,l)))

# def my_func(func,l):
#     new_list=[]
#     for i in l:
#         new_list.append(func(i))
#     return new_list

# def square(a):
#     return a**2
# l=[1,2,3,4]
# print(my_func(square,l))


def my_func(func,l):
    new_list=[]
    for i in l:
        new_list.append(func(i))
    return new_list

def my_func2(func,l):
    return [func(i) for i in l]

l=[1,2,3,4]

print(my_func(lambda x: x**2,l))
print(my_func2(lambda x: x**2,l))