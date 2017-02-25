from tkinter import Tk
from tkinter.filedialog import askopenfilename
Tk().withdraw()

print("Welcome to Sentest Counter")
print("This program will tell you how many senteces you have more than 3 and less than 8 characters")
print("Lets get started")

def main():
    try:
        numWords = 0
        count=0
        a = input("Enter 'Yes' to continue or 'No' to exit:")
        if a.lower()=="yes":
            f=askopenfilename()
            with open(f,"r")as file:
                for line in file:
                    wordsList = line.split()
                    numWords += len(wordsList)

                for i in range(len(wordsList)):
                    k=wordsList[i]
                    if 3<= len(k) <=8:
                        count += 1
                    i+=1
                per = open(f, 'r').read().count(".")
                com = open(f, 'r').read().count(",")
                semi = open(f, 'r').read().count(";")
                exc = open(f, 'r').read().count('!')
                ques = open(f, 'r').read().count('?')
                col = open(f, 'r').read().count(":")
                sentences = per + com + semi + exc + ques + col
                average = count / len(wordsList)

                print("Number of words you have is", count)
                print('Average words is {}'.format(average))
                print("Sentences: ", sentences)
        elif a.lower() == "no":
            print("Goodbye")
        elif a.lower() != "yes" or "no":
            print("Please enter Yes or No")
            main()
    except:
        main()
main()