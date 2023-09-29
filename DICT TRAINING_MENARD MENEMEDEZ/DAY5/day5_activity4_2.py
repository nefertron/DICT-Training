
from day5_activity4 import BankAccount

acc1 = BankAccount('Menard', 20)
acc2 = BankAccount('Gem Rey')

acc1.deposit(20)
acc2.deposit(50)

acc1.withdraw(21)
acc2.withdraw(20)

acc1.check_balance()
acc2.check_balance()