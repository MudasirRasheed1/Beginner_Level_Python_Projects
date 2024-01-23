choice = 'y'
while choice == 'y' or choice == 'Y': 
    lower_number = 1
    upper_number = 9
    print(f"\n\nGuess a number between {lower_number} and {upper_number} both inclusive")
    print("Click enter when you are ready")
    input()
    print("\n\nNow multiply the number by 3 and remember the result") 
    print("Click enter when you are ready")
    input()
    
    print("\n\nAgain multiply the result by 3 and remember the result")
    print("Click enter when you are ready")
    input()
    char = None
    while True:
        try:
            char = input("\nEnter y if your number is a single digit number else enter n: ")
            if char not in ['y','n','Y','N']:
                raise Exception
            break
        except Exception:
            print("Enter a valid input")
            continue


    if char in ['y', 'Y']:
        print("The number you have in your mind is 9")
    else:
        print("The sum of digits of the number you have in your mind is 9")
    print("\n\nwasn't that cool?")
    print("Enter y to play again or n to exit")
    choice = input("Enter your choice: ")


