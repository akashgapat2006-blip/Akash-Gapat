# Akash-Gapat
pine = 1212
attempts = 3
balance = 1000

while attempts > 0:       #To check attempts
    userPin=int(input("Enter Your Pin : "))

    if userPin == pine:
        print("Welcome to Akash ATM APP")
        while True:
            print("ATM MENU ..")
            print("1. Deposit")
            print("2. Withdrwa")
            print("3. Check Balance")
            print("4. Exit")
            choice =int(input("Enter your choice : "))
            if choice == 1:
                deposit=int(input("Enter amount to deposit: "))
                if deposit > 0:
                    balance += deposit
                    print("Amount deposited successfully , New balance is: ", balance)
                else:
                    print("Invalid amount") 
            elif choice == 2:
                withdraw=int(input("Enter amount to withdraw: "))
                if withdraw > 0:
                    if withdraw <= balance:
                        balance -= withdraw
                        print("Amount withdrawn successfully, New balance is: ", balance)
                    else:
                        print("Insufficient balance")
                else:
                    print("Invalid amount")
            elif choice == 3:
                print("Your current balance is: ",balance)
            elif choice == 4:
                print("Thank you for using Akash ATM APP")
                break #END THE LOOP        
            else:
                print("Incorrect choice")
    else:
        attempts -= 1
        print("Incorrect Pin")                               
                 
                              
