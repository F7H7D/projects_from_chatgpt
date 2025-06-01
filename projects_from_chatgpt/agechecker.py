print("Your age will shown by 2025.")

bdate = int(input("Enter your birth year : "))

age = 2025 - bdate

if (age < 18):
    print(f"Your age is {age},you are less than 18 so don't miss your school.")
else:
    print(f"Your age is {age},you are more than 18 it's good for you.")