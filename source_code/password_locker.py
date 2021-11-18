# a secure password locker program
password = {}
greeting = input("Hello, there.\nWelcome to the password locker.\nDo you want to input new password today?\nEnter 'exit' to quit the program.\n")

while greeting.lower() != 'exit':
    account_name = input("Please enter your account name: ")
    code = input("Enter your passcode: ")
    password.setdefault(account_name, code)
    greeting = input("Do you have more passwords to save?\nEnter 'exit' to quit the program.\n")
    continue

print(password)