
while True:
    n1 = int(input("Enter number 1 : "))
    n2 = int(input("Enter number 2 : "))

    opn = input("Choose operation (+,-,*,/) : ")

    if opn == "+":
        result = n1+n2
    elif opn == "-":
        result = n1-n2
    elif opn == "/":
        if n2 == 0:
            print("⚠️ Cannot divide by 0.")
            continue 
        result = n1/n2
    elif opn == "*":
        result = n1*n2
    else:
        print("You have choosen wrong operation, choose between (+,-,*,/)")
        continue
    print(f"RESULT of {n1}{opn}{n2}= {result}\n")
    run = input("Do you want to calculate again? (yes/no): ")
    if run.lower() != "yes":
        print("Calculator closed.\n")
        break