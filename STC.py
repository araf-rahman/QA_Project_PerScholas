print("Welcome to Sentest Counter")
def main():
    a = input("Enter yes/no to continue")
    if a=="yes":
        import tkinter as tk
        from tkinter import filedialog
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename()
    elif a=="no":
        print("Goodbye")
    import re
    print()
    count = len(re.findall(r'\w+', line))
    print ("The number of words in this paragraph:", count)
main()