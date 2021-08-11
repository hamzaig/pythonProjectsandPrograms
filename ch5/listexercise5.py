def fin(l1,l2):
    out=[]
    for i in l1:
        if i in l2:
            out.append(i)
    return out

print(fin([1,2,3,4,5],[4,5,6,7,8,9]))