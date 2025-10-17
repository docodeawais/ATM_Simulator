import json
import random
import os

class ATM:

    def create_account(self):
        account = {}

        name = input("Enter Your Name: ")
        account_no = random.randint(3000, 10000)
        account_balance = 0
        account_pin = input("Enter Your Pin")

        filename = "atm.json"

        
        if not os.path.exists(filename):
            with open(filename, "w") as f:
                json.dump([], f)

        with open(filename, "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []

    
        if data:
            last_id = data[-1]["id"]
        else:
            last_id = 0

        account["id"] = last_id + 1
        account["name"] = name
        account["account_no"] = account_no
        account["account_balance"] = account_balance
        account["account_pin"] = account_pin

        
        data.append(account)
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)

        print(f"\n✅ Account Created Successfully!")
        print(f"Account No: {account_no}")
        print(f"Balance: {account_balance}")

    def desposit(self):
        pin = input("Enter Your Pin: ")
        with open("atm.json", "r") as f:
            try:
                account = json.load(f)
                for record in account:
                    if pin == record['account_pin']:
                        deposite = float(input("Enter Desposite Amount: "))
                        record['account_balance'] += deposite
                        print(f"✅Deposit Successfull Your account balance is : {record['account_balance']}")
                        with open("atm.json", "w") as f:
                            json.dump(account, f, indent=4)
                            break
            except:
                print("Error") 


    def withdraw(self):
        pin = input("Enter Your Pin: ")
        with open("atm.json", "r") as f:
            try:
                account = json.load(f)
                for record in account:
                    if pin == record['account_pin']:
                        withdraw = float(input("Enter Withdraw Amount: "))
                        record['account_balance'] -= withdraw
                        print(f"✅Withdraw Successfull Your remaining balance is : {record['account_balance']}")
                        with open("atm.json", "w") as f:
                            json.dump(account, f, indent=4)
                            break
            except:
                print("Error")  
    
    def check_balance(self):
        pin = input("Enter Your Pin: ")
        with open("atm.json", "r") as f:
            accounts = json.load(f)
            for record in accounts:
                if pin == record['account_pin']:
                    print(f"Your Account Balance is: {record['account_balance']}")
                else:
                    print("Invalid Pin")



Machine = ATM()
i=0
while(i==0):
    print("Wellcome to ATM\n")

    print("1. Check Account Balance")
    print("2. Deposite Amount")
    print("3. Withdraw")
    print("4. Create Account")
    print("5. Exit")
    choice = input("Enter Your Choice: ")

    if choice == '1':
        Machine.check_balance()
    elif choice == '2':
        Machine.desposit()
    elif choice == '3':
        Machine.withdraw()
    elif choice == '4':
        Machine.create_account()
    elif choice == '5':
        print("Good Bye :)")
    else:
        print("Invalid Choice")



