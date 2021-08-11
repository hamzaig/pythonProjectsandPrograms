name=input("Please Enter Your Name: ")
i=0
while i<len(name):
    count = name.count(name[i])
    print(name[i])
    print(str(count).rstrip(" "))
    i+=1

