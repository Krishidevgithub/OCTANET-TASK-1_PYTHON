import time

print("******************************<WELCOME TO PY-ERA BANK>*********************************")
print(" ")

print("Please enter your ATM CARD")
print("____________________________________________________________________________")
time.sleep(2)  # It will take 2 seconds to process
print("Please Wait! while reading your Chip Data...")
print("____________________________________________________________________________")
time.sleep(4)  # It will take 4 seconds to read the chip data

password = 2024  # 4-digit password to match with PIN
chances = 3  # Total unsuccessful chances
balance = 7000  # Amount present in the account

while chances != 0:  # Users can make transactions more than once
    try:
        pin = int(input("Enter your 4-digit Card PIN: "))  # Asks to enter the password
        print("____________________________________________________________________________")
        time.sleep(2)  # Take 2 seconds for processing as in real ATMs
        if pin == password:  # If password matches the user's PIN
            print("Please select your Transaction")
            print("____________________________________________________________________________")
            # List of Transactions
            print("""
    1==Balance Enquiry
    2==Withdrawal
    3==Deposit
    4==PIN Change
    5==Exit
     """)
            option = int(input("Enter your Choice: "))
            print("**************************")

            if option == 1:  # BALANCE ENQUIRY
                print(f"Your current balance is {balance}")
                print("THANK YOU")
                print("____________________________________________________________________________")
            elif option == 2:  # WITHDRAWAL
                withdraw_amount = int(input("Please enter the amount you want to withdraw: "))
                if withdraw_amount > balance:  # If withdrawal amount is more than available balance
                    print("Transaction Failed!! Insufficient Balance...")
                    print("THANK YOU!!")
                    print("____________________________________________________________________________")
                else:
                    print("Please wait while your transaction is processing...")
                    print("____________________________________________________________________________")
                    time.sleep(5)
                    balance -= withdraw_amount
                    print("Transaction History")
                    print("****************************************************************************")
                    print("Date:xx-xx-24")
                    print("Time:xx:xx hrs")
                    print(f"{withdraw_amount} is debited from your account")
                    print(f"Available Balance: {balance}")
                    print("THANK YOU!!")
                    print("____________________________________________________________________________")
            elif option == 3:  # DEPOSIT
                deposit_amount = int(input("Enter the amount to be deposited to your account: "))
                print("Please wait while your transaction is processing...")
                print("____________________________________________________________________________")
                time.sleep(5)
                balance += deposit_amount
                print("Transaction History")
                print("****************************************************************************")
                print("Date:xx-xx-24")
                print("Time:xx:xx hrs")
                print(f"{deposit_amount} is successfully credited to your account")
                print(f"Available Balance: {balance}")
                print("THANK YOU!!")
                print("____________________________________________________________________________")
            elif option == 4:  # PIN GENERATION
                print("Generate a new PIN")
                print("----------------------------------------------------------------------------")
                new_pin = int(input("Enter your new 4-digit PIN: "))
                print("Please Wait....")
                time.sleep(5)
                password = new_pin
                print("Your new PIN is successfully generated")
                print("THANK YOU!!")
                print("____________________________________________________________________________")
            elif option == 5:  # EXIT
                print("----------------<THANK YOU!!>---------------")
                break
            else:  # INVALID OPTION
                print("Invalid option! Please choose a correct option and try again...")
                print("THANK YOU!!")
                print("____________________________________________________________________________")
        else:  # LIMITATION OF CHANCES
            chances -= 1
            if chances == 0:  # CARD BLOCKED
                print("You have entered the wrong PIN 3 times. Your card is blocked.")
                print("##############################################################")
            else:  # ALERT!
                print(f"WRONG PIN! Please enter a valid PIN. You have {chances} chances left.")
                print("____________________________________________________________________________")
    except ValueError:  # Handling non-integer inputs for PIN and choices
        print("Invalid input! Please enter a valid number.")
        print("____________________________________________________________________________")
