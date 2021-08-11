l1=[1,7,3,4,5]
l2=[6,2,8,9,10]
# l=[(1,6),(2,7),(3,8),(4,9),(5,10)]
# print(list(zip(*l)))
# l3,l4=list(zip(*l))
# print(l3)
# print(l4)
# print(list(l3))
# print(list(l4))
listt=[]
for i in zip(l1,l2):
    listt.append(max(i))
print(listt)