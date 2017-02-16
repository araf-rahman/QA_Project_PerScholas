input_set = list()
num = None
while num is None:
    ret = input("Enter how many elements you want:")
    try:
        num = int(ret)
    except ValueError:
        print("Invalid input, please enter a digit.")

print("Enter numbers in array:")
for i in range(num):
    n = None
    while n is None:
        ret = input("input number :")
        try:
            n = int(ret)
            input_set.append(n)
        except ValueError:
            print("Invalid input, please enter a digit.")

print("ARRAY: ", input_set)

largest=-1
for i in input_set:
    if i > largest:
        largest = i
smallest = input_set[0]
for i in range(len(input_set)):

    if input_set[i] < largest:
        smallest = input_set[i]

print("Largest number is :",largest)
print("Smallest number is", smallest)