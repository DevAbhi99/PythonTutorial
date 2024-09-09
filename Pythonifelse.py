age=input("What us your age?")

if (int)(age)<0:
    print("Invalid input!")
else:
    if (int)(age)>=18:
        print("Eligible to vote!")
    else:
        print("Ineligible to vote!")
