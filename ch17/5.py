while True:
    try:
        age=int(input("Please Enter Your Age"))
        break
    except ValueError:
        print("May b you enter a String")
    except:
        print("Unexpected Error")

if age<18:
    print("You Can't Play")
else:
    print("You can Play")

