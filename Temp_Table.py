start = 0
end = 101
increment = 5

def main():
    print('The following table shows conversion of Celsius to Farenheit')
    print( 'between 0 and 100 degrees Celsius.')
    print('')
    print('Celsius\t   Farenheit')
    print('____________________')
    #convert celsius input to farenheit using loop
    for Celsius in range (start, end, increment):
        Farenheit = int((9/5) * Celsius + 32)
        print(Celsius, '\t', format(Farenheit))
main()

