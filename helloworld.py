print("Welcome, this program will find the average of a list of numbers you enter.")

numbers = input("Enter your numbers, seperated by spaces.")

print("You have entered")

print(numbers)

print(numbers[0])
print(numbers[1])
print(numbers[2])
print(numbers[3])
print(numbers[4])
print(numbers[5])
print(numbers[6])

print(len(numbers))
average = 0
sum = 0
for n in numbers:
    sum = sum + n
average = sum / len(numbers)
print("The average of the above numbers is: ")