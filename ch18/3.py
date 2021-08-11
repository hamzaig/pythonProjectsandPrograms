with open("salary.txt","r") as rf:
    with open('output.txt','a') as wf:
        for l in rf.readlines():
            name,salary=l.split(",")
            wf.write(f"{name}\'s salary is {salary}")
            