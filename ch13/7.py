def avg_finder(*args):
    new_list=[]
    for pair in zip(*args):
        new_list.append(sum(pair)/len(pair))
    return new_list
print(avg_finder([1,2,3],[4,5,6],[7,8,9]))