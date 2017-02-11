input_set = list()
num = None
while num is None:
    ret = input("Enter how many elements you want:")
    try:
        num = int(ret)
    except ValueError:
        print ("Invalid input, please enter a digit.")

print("Enter numbers in array:")
for i in range(num):
    n = None
    while n is None:
        ret = input("input number :")
        try:
            n = int(ret)
            input_set.append(n)
        except ValueError:
            print ("Invalid input, please enter a digit.")

print ("ARRAY: ", input_set)
print ("Largest number is :", max(input_set))
print ("Smallest number is :", min(input_set))