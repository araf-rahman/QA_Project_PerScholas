def main() :
    b = int(input("number pls: "))
    sum = 0
    for i in range (0, b) :
        z = int(input("Enter a number "))
        print("Number %d is %d" % (i+1,z))
        sum = sum + z
    print ('The average is %d ' % (sum/b))

main()