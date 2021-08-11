


def chk(num1,num2):
    if num1>num2:
        return num1
    return num2

num1,num2=input("Please Enter the two numbers").split(" ")
num1=int(num1)
num2=int(num2)
print(chk(num1,num2))