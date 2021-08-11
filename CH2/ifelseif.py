# number=9
# playernum=int(input("Please Enter Any Number"))
# if playernum==number:
#     print("You Win")
# else:
#     if playernum<number:
#         print("Enter Number is Low")
#     else:
#         print("Enter Number is High")
    

name,age=input("Enter Your Age and Name With Space").split(" ")
age=int(age)
if (name[0]=="a" or name[0]=="A") and age>10:
    print("Yes")
else:
    print("No")     