
from accounts import create_account , del_account , check_balance
from transcations import deposit , withdraw
 

bank_open = True


def create_bank_account():   
    print('Enter your details to create your bank account')
    name  = input('Enter your name : ')
    password =  input('Enter your passowrd :')
    amount = int(input('Enter your payment'))
    create_account(name , password , amount)


def check_bank_bal():
    print('Enter your detail to check your balance : ')
    name = input('Enter your name : ')
    check_balance(name)


def deposit_money():
    print('Enter your details to deposit money')
    name = input('Enter your name :')
    password = input('Enter your password :')
    amount = int(input('Enter your amount to deposit :'))
    deposit(name, password , amount)

def withdraw_money():
    print('Enter your details to withdraw money')
    name = input('Enter your name :')
    password = input('Enter your password :')
    amount = int(input('Enter your amount to withdraw :'))
    withdraw(name, password,amount)

def delele_bank_account():
    print('Enter your details to delete bank account')
    name = input('Enter your name :')
    password = input('Enter your password :')
    del_account(name,password)
    

while bank_open:
    print("Enter any options to continue \nBank is open")
    print("1.To create bank account \n2.To check balance " \
    "\n3.To deposit money \n4.To withdraw money " \
    "\n5.To delete account \n6.To close bank")
    option = int(input('Enter the option : '))
    match option:
        case 1 :
            create_bank_account()
        case 2 :
            check_bank_bal()
        case 3 :
            deposit_money()
        case 4 :
            withdraw_money()
        case 5 :
            delele_bank_account()
        case 6 :
            bank_open = False
        case _ :
            print("option not matches")
    

print("Bank is closed")



