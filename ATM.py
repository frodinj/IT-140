import sys

#ACCT BALANCE VARIABLE
#defines account balance 
account_balance = float(500.25)


#<--------functions go here-------------------->
#printbalance function defines what the print will do under input B
def printbalance (account_balance, userchoice):
  return account_balance

#deposit function
#defines how money is deposited as a general rule
#uses the deposit amount and account balance to determine the 
#new balance.

def deposit (deposit_amount, account_balance):
  return deposit_amount + account_balance

#withdraw function
#defines how money is withdrawn as a general rule
#uses the withdrawal amount and account balance
#to determine the new balance.

def withdrawal (withdrawal_amount, account_balance):
  return  account_balance - withdrawal_amount


#USER INPUTS
#Conditional statements that tell what functions to call based
#on the user input.
#inputs available and accounted for are Q, D, W, and B.
#

userchoice = input ("What would you like to do?\n")

if (userchoice == 'D'):
  deposit_amount = float(input('How much would you like to deposit today?\n'))
  #account_balance = account_balance + deposit_amount
  #this code was an error that I wanted to leave in as a reference
  #and reminder of what not to do.
  account_balance = deposit(deposit_amount, account_balance)
  print('Deposit was ', '$%.2f' %deposit_amount, ', current balance is ', '$%.2f' %account_balance)
if (userchoice == 'B'):
  #This is the call for the function. It is repeated in the other blocks
  #and it adjusts the account balance to reflect the function that
  #is called.
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