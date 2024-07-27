def show_menu():
    print("*********Menu************")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Money Transfer")
    print("5. Exit")
    print("**************************")

def main():
    balance = 5000

    while True:
        show_menu()
        option = int(input("Option: "))
        
        if option == 1:
            print(f"Balance is: ${balance}")
        elif option == 2:
            deposit_amount = float(input("Deposit Amount: "))
            balance += deposit_amount
            print(f"Total Amount: ${balance}")
        elif option == 3:
            withdraw_amount = float(input("Withdraw Amount: "))
            if withdraw_amount <= balance:
                balance -= withdraw_amount
                print(f"Total Amount: ${balance}")
            else:
                print("Not Enough Money")
        elif option == 4:
            transfer_amount = float(input("Transfer Amount: "))
            if transfer_amount <= balance:
                balance -= transfer_amount
                account_number = input("Enter Account Number: ")
                print("Transfer Successfully")
                print(f"Total Amount: ${balance}")
            else:
                print("Not Enough Money")
        elif option == 5:
            print("******Thank you So Much, Have A Nice Day********")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
