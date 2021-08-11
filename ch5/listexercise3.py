def reve(l):
    el=[]
    for i in l:
        el.append(i[::-1])
    return el

l=['abc','def','ghi','jkl']
print(reve(l))

