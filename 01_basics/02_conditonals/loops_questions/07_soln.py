# keep asking user input until they enter number between 1-10:
while True:
    num= int(input("enter your number between 1 to 10"))

    if 1<= num<=10:
        print("thanks")
        break
        
    else:
       print("give a right input")        
        
