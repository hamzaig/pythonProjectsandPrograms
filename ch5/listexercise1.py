# 1st solution

# def rev(l):
#     l.reverse()
#     return l
# x=list(range(1,5))
# print(rev(x))

    # 2nd Solution

# def rev(l):
#     return l[::-1]

def rev(l):
    rev=[]
    for i in range(len(l)):
        pup=l.pop()
        rev.append(pup)
    return rev

x=list(range(1,5))
print(rev(x))