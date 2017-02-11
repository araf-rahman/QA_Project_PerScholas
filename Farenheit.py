def main():
    temp = input("Enter temperature in Fahrenheit? (e.g., 45,) : ")
    degree = int(temp[:-1])
    result = int(round((degree - 32) * 5 / 9))
    print("The temperature you enter is ", temp, "in", result, " Celsius.")

    a = input("Enter yes/no to continue")
    if a == "yes":
        main()
    elif a == "no":
        print('Good bye')
main()