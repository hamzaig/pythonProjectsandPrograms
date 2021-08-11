def sublists(l):
    counter=0
    for i in l:
        if type(i)==list:
            counter+=1
    return counter

li=[1,2,[1,2,3],1,2,3]
print(sublists(li))