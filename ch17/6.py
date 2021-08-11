while True:
    try:
        age=int(input("Please Enter A Number"))
    except ValueError:
        print("Please Type Integer")
    except:
        print("unexpected Error")
    else:
        print(f"user input = {age}")
        break
    finally:
        print("Finally Block.........")