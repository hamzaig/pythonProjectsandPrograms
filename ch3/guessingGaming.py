import random
winning_number=random.randint(1,100)
tries=0
while True:
    input_number=int(input("Please Enter The Number Between 0 & 100"))
    if input_number<winning_number:
        tries+=1
        print("Too Low")
        continue
    elif input_number>winning_number:
        tries+=1
        print("Too High")
        continue
    else:
        print(f"you win and you gussed the number in {tries} times")
        break


    
