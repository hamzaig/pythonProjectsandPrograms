# number=[1,2,3,4,5,6]
# print(min(number))
# print(max(number))

# names=['Hamzaali','Ali','Khalid']
# print(max(names)) #do nothing

# def func(name):
#     return len(name)
# names=['Hamzaali','Ali','Khalid']
# print(max(names,key=func))

# def func(name):
#     return len(name)
# names=['Hamzaali','Ali','Khalid']
# print(min(names,key=func))

# names=['Hamzaali','Ali','Khalid']
# print(min(names,key=lambda name: len(name)))
# print(students[0].get('age')) for only concept

# students=[
#     {'name':'hamza','score':55,'age':24},
#     {'name':'ali','score':64,'age':18},
#     {'name':'khalid','score':96,'age':17}
# ]
# print(max(students,key=lambda x: x.get('age'))['age'])

students={
    "hamza"     : {'score':55,'age':24},
    "Ali"       : {'score':64,'age':18},
    "Khalid"    : {'score':96,'age':17}
}
print(max(students,key=lambda item: students[item]["score"]))