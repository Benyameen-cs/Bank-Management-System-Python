
from data import banks_acounts

def create_account(name : str , password : str , amount = 0):
    if name and password:
        bank_user_data = {
            "name" : name ,
            "password": password ,
            "amount" : amount,
        }
        banks_acounts.append(bank_user_data)
        print(f"your are acount is created successfully mr {name }.")
        return None
    else:
        print(f"plz enter your name and password.")


def check_balance(name : str):
    if name:        
        for i in range(0,len(banks_acounts)):
            data = banks_acounts[i]
            if data["name"] == name:
                bal = data["amount"]
                print(f'Your current balance is : {bal}')
                return None  
        print('no acount found')
    if not name:
        print('Name required')


def del_account(name : str , password :str):
    for i in range(0,len(banks_acounts)):
        if i == None:
            print('Zero Bank Users...')
        data = banks_acounts[i]
        if data['name'] == name and data['password'] == password:
            banks_acounts.pop(i)
            print(f"bank account is delete {data["name"]}")
            return



