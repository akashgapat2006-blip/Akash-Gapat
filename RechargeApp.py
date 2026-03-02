# Recharge Application System
    
while True:
        print("Available Recharge Plans")
        print("1. 149 - 18 days, 1GB/day")
        print("2. 199 - 28 days, 1.5GB/day")
        print("3. 999 - 84 days, 2GB/day")
        print("4. Exit")
        choice = input("Select a plan (1-4): ")
        if choice == "1":
            print("You selected 149 plan")
        confirm = input("Confirm payment? (yes/no): ")
        if confirm.lower() == "yes":  
            print("Payment successful Recharge done for ₹99 plan")
        else:
            print("Payment cancelled.")
        if choice == "2":
            print("You selected 199 plan")
        confirm = input("Confirm payment? (yes/no): ")
        if confirm.lower() == "yes":
            print("Payment successful Recharge done for ₹199 plan")
        else:
            print("Payment cancelled.")
        if choice == "3":
            print("You selected 999 plan")
        confirm = input("Confirm payment? (yes/no): ")
        if confirm.lower() == "yes":    
            print("Payment successful Recharge done for ₹299 plan")
        else:
            print("Payment cancelled")
        if choice == "4":
            print("Thank you for using the Recharge System")
            break
        else:
            print("Invalid choice Please try again")

# Run the application
