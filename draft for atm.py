import sys

#ACCT BALANCE VARIABLE
#defines account balance 
account_balance = float(500.25)


#<--------functions go here-------------------->
#printbalance function
def printbalance (account_balance, userchoice):
  return account_balance

#deposit function

def deposit (deposit_amount, account_balance):
  return deposit_amount + account_balance



#withdraw function

def withdrawal (withdrawal_amount, account_balance):
  return  account_balance - withdrawal_amount


#User Input goes here, use if/else conditional statement to call function based on user input

userchoice = input ("What would you like to do?\n")

if (userchoice == 'D'):
  deposit_amount = float(input('How much would you like to deposit today?\n'))
  #account_balance = account_balance + deposit_amount
  account_balance = deposit(deposit_amount, account_balance)
  print('Deposit was ', '$%.2f' %deposit_amount, ', current balance is ', '$%.2f' %account_balance)
if (userchoice == 'B'):
  account_balance = printbalance(account_balance, userchoice)
  print('Your current balance: ', '$%.2f' %account_balance)
if (userchoice == 'W'):
  withdrawal_amount = float(input('How much would you like to withdraw today?\n'))
  if withdrawal_amount > account_balance:
    print('$%.2f' %withdrawal_amount, 'is greater than your account balance of ', '$%.2f'%account_balance)
  else:
    account_balance = withdrawal(withdrawal_amount, account_balance)
    print('Withdrawal amount was ', '$%.2f' %withdrawal_amount, ', current balance is ', '$%.2f' %account_balance)
if userchoice == 'Q':
  print('Thank you for banking with us.')