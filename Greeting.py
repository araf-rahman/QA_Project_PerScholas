while True:
    name = input("What is your name?")
    print ("Nice to meet ya "+ name  )
    color = input("What is your favorite color?")
    print ("That's a nice color")
    food = input("What is your favorite food?")
    print ( food + " sounds yummy")
    a = input("Enter yes/no to continue")
    if a=="yes":
        continue
    elif a=="no":
        print("Enter either yes/no")