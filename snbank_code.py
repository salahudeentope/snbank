import random
import os
import json
import string
import re


start = True
while start:
    print("Welcome to Our-People Bank Plc Banking System \n")
    print("1 Staff Login")
    print("2 Close App")
    start_option = input("Please enter your selection:[1/2] ")
    while start_option not in ["1", "2"]:
        start_option = input("kindly enter a valid selection [1 or 2]: ")
    if start_option == "1":
        employee_username = input('kindly input your staff username: ')
        employee_password = input('kindly input your staff password: ')
        with open('staff.txt') as staff:
            staff_details = json.load(staff)
            for employee in staff_details:
                if employee['username'] == employee_username and employee['password'] == employee_password:
                    session_created = open('session.txt', 'w')
                    session_created.write(employee_username)
                    session_created.close()

                    logged_in = True
                    print(f"\nWelcome {employee_username}")
                    customers = []
                    while logged_in:
                        print("what transaction would you like to do? Please select from the listed "
                              f"options \n ")
                        print("1. Create new bank account")
                        print("2. Check Account Details")
                        print("3. Logout")
                        staff_choice = input("Please enter your selection:[1/2/3] ")
                        while staff_choice not in ["1", "2", "3"]:
                            staff_choice = input("kindly enter a valid selection [1/2/3]: ")
                        if staff_choice == '1':

                            print('kindly input the following customer details')
                            account_name = input('Name: ')
                            while True:
                                try:
                                    account_balance = float(input('Opening Balance: '))
                                except ValueError:
                                    print("Please input a valid number")
                                    continue
                                else:
                                    break
                            account_type = input('Account Type: ')
                            email = input('Email: ')
                            while not bool(re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email)):
                                email = input("Please input a valid email: ")
                                continue
                            account_number = ''.join(random.choice(string.digits) for _ in range(10))

                            customer_details = {
                                'Account_name': account_name,
                                'Opening_balance': f"NGN {account_balance}",
                                'Account_type': account_type,
                                'Customer_email': email,
                                'Account_number': account_number
                            }
                            customers.append(customer_details.copy())

                            with open('customer.txt', 'w') as file:
                                json.dump(customers, file)
                            print(f"The customer's account number is : {account_number}")

                        elif staff_choice == '2':
                            account_num = input("please enter the customer's account number: ")
                            with open('customer.txt', 'r') as customers_file:
                                loaded_customers = json.load(customers_file)
                                for customer in loaded_customers:
                                    if customer['Account_number'] == account_num:
                                        print()
                                        for i, j in customer.items():
                                            print(f"{i}: {j}")
                        else:
                            os.remove("session.txt")
                            print(f"\nThank you {employee_username} you've been successfully signed out.")
                            logged_in = False

    else:
        print("\nThank you for choosing to work at Our-People bank")
        start = False
