import random


while True:
    prmson = input("Enter(yes\\no) : ")
    if prmson.lower() == "yes":
        dice = random.randint(1,6)
        print(f"You rolled=",dice)
        if dice == 6 :
            print("wooo!you got one eye")
    elif prmson.lower() == "no":
        print("As your wish .")
        break    
    else:
        print("input only 'yes'or'no'.")


