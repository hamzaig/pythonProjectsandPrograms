def func(l,**kwargs):
    if kwargs.get("rev_str")==True:
        return [i[::-1].title() for i in l]
    else:
        return [i.title() for i in l]
    

name = ['hamza','ali']
print(func(name,rev_str=True))
