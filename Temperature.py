temperature = int(input("What is the temperature?"))
if 60 < temperature < 90:
    print("It is Warm.")
elif temperature >= 90:
    print("It is hot.")
elif temperature <= 60:
    print("It is chilly.")