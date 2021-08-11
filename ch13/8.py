# n1=[2,4,6,8,10]
# n2=[1,2,3,4,5,6]
# n3=[]
# for i in n1:
#     if i%2==0:
#         n3.append(True)

# print(n3)

# n1=[2,4,6,8,10]
# n2=[1,2,3,4,5,6]
# n3=[]
# for i in n1:
#         n3.append(i%2==0)
# print(n3)

# print(all([True, True, True, True, True]))
# print(all([True, False, True, True, True]))

n1=[2,4,6,8,10]
n2=[1,2,3,4,5,6]
# print
print(all([i%2==0 for i in n2]))
print(any([i%2==0 for i in n2]))