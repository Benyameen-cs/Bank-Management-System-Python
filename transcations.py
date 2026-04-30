
from data import banks_acounts

def deposit(name :str , password : str , amount : int) -> int :
    for data in banks_acounts:
        if data["name"] == name and data["password"] == password :
            bal = (int(data["amount"])) + amount
            data["amount"] = bal
            print(f'you deposit ${amount} your new balance is :${bal}')
            return None
    else:
        print("no account found")


def withdraw(name:str , password: str, amount :int):
    for data in banks_acounts:
        if data["name"] == name and data["password"] == password :
            if data["amount"] < amount:
                print('your balance is insuffient to withdraw')
            elif data["amount"] >= amount:
                bal = (int(data["amount"])) - amount 
                data["amount"] = bal
                print(f'you withdraw : ${amount}\nyour new balance is :${bal}')
                return None
    else:
        print("no account found")
    

