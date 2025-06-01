print("~~~🧾QUIZE GAME🧾~~~\n")
i = 1
j = 1
f = 1
score = 0

print("=====Quize-1=====\n")
print("What is capital of East Pakistan in 1971,08,17 ?\n")
print("A|Dhaka,B|Lahore,C|Kolkata,D|Paris\n")
while (i < 3):
    qz1 = input("Choose between A\\B\\C\\D : ")

    if qz1.upper() == "B":
        print("You are right!GENIUS🧠✔\n")
        score += 1
        break 
    else:
        print("CHANCE = 2\\",i)
    i += 1
print("====Quize2====\n")
print("Where Bongobhobon is located ?")
print("A|Bogura,B|Tangail,C|Bhola,D|Dhaka\n")
while (j<3):
    qz2 = input("Choose between A\\B\\C\\D : ")

    if qz2.upper() == "D":
        print("You are really a GENIUS!!✔🐱‍🏍\n")
        score += 1
        break
    else:
        print("CHANCE : 2\\",j)
    j += 1
print("====Quize3====\n")
print("Who is \'\'Mlak al-mawt\'\'?\n")
print("A|Angel of massage,B|Angel of mercy,C|Angel of death,D|Angel of trumpet\n")
while (f<3):
    qz2 = input("Choose between A\\B\\C\\D : ")

    if qz2.upper() == "C":
        print("REDICULAS🎇!!You are a G.O.A.T!!✔🐐🐐\n")
        score += 1
        break
    else:
        print(f"CHANCE : 2\\{f}\n")
    f += 1
print(f"Your marks is 3\\{score}\n")
print(f"Your score is = {score}\n")

if score == 1:
    print("You have to study alot.\n")
elif score == 2:
    print("Good,but you have to be more better.\n")
else:
    print("I have just one word to say \'\'G.O.A.T🐐🐐\'\'\n")

