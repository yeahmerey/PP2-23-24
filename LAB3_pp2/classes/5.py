class Account():
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0

    def checkBal(self):
        print(f"\n{self.balance} тенге бар.\n")

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} тенге салынды депозитке.\n")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Акша жетпейд.\n")
        else:
            self.balance -= amount
            print(f"{amount} тенге алынды с депозита.\n")


onlineBank = True
name_of_deposit = Account(input('Напишите имя для вашего аккаунта.\n'))
while onlineBank:
    a = (input("Если хочешь снять деньги снять с депозита деньги, отправь 1. \nЕсли хочешь положить деньги в депозит, отправь 2. \nЕсли хочешь проверить баланс, отправь 3.\nЕсли хочешь отключить код, отправь 4.\n"))
    if a == '1':
        try:
            name_of_deposit.withdraw(int(input('\nУкажите сколько денег хотите снять.\n')))
        except:
            print("\nError\n")
            pass
    if a == '2':
        try:
            name_of_deposit.deposit(int(input('\nУкажите сколько денег хотите положить.\n')))
        except:
            print("\nError\n")
            pass
    if a == '3':
        name_of_deposit.checkBal()
    if a == '4':
        onlineBank = False
    if a not in ['1', '2', '3', '4']:
        print('\nПожалуйста выберите из списка.\n')
        continue