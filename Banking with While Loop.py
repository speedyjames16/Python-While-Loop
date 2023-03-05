def print_menu():
    print(      "Welcome to American Banking")
    print("")
    print("What would you like to do today?")
    print("1. Withdraw Funds")
    print("2. Deposit Funds")
    print("3. Check Balance")
    print("4. Exit\n")
print_menu()

while True:
    print_menu()
    banking = input("Pick a number \n> ")
    funds = 50

    if banking == "1":
        withdrawal_amount = eval(input("Enter amount in dollars you'd like to withdraw "))
        if withdrawal_amount <= funds:
            funds -= withdrawal_amount
            print("Your money is printing, your new balance is " + str(funds)+ " Dollars\n")
            print("Returning to main menu...")
            

        else:
            print("Not enough balance, Try again")
            continue
            
    if banking == "2":
        deposit_amount = eval(input("Enter amount in dollars you'll be depositing "))
        print(deposit_amount)
        funds += deposit_amount
        print("Thanks for your deposit, your new balnce is " +str(funds) + " Dollars")
        continue
        
    if banking == "3":
        print ("Your balance is $" + str(funds) + " dollars\n")
        print ("Thank you, Have a Great Day")
        quit()
    
    if banking =="4":
        print ("Leaving American Banking")
        quit()
    
