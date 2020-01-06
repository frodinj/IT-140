

'''
The task is broken down into three sections.
Section 1 - User Input
Section 2 - loop through the grocery list
Section 3 - provide output to the console
'''

# CREATE DICT AND LIST
# here I create a dictionary to store the items and a list to
# store the history of groceries

grocery_item = {}

grocery_history = []
#VARIABLE
#Here I create a variable that will be used to stop the while loop
#when the user is done entering items.

stop = False

# WHILE LOOP
# Here is the while loop that collects relevant information and 
# creates the items in the history list.
while not stop:
    #Name
    name = input("Item name:\n")
    #Qty
    quantity = input("Quantity purchased:\n")
    #Cost
    cost = input("Price per item:\n")
    #Item Variable for Dict
    grocery_item = {'item_name':name, 'item_quantity':int(quantity), 'item_cost':float(cost)}
    #Add to dictionary
    grocery_history.append(grocery_item)
    #Determines variable to stop the while loop.
    finished = input("Would you like to enter another item?\nType 'c' for continue or 'q' to quit:\n")
    if finished == 'q':
      stop = True

#VARIABLE
#for grand total

grand_total = 0

#FOR LOOP
#This section takes the costs and attributes and applies them
#to the history to generate the final output.  

for item in grocery_history:
  
  #Calculates Cost
  item_total = item['item_quantity']*item['item_cost']
  #Keeps a running grand total.
  grand_total += item_total
  #Format example for output (template):
  #2 item	@	$1.49	ea(cost)	$2.98(total)
  print("%d %s @ $%.2f ea $%.2f" %(item['item_quantity'], item['item_name'], item['item_cost'], item_total))
  
  #RESET ITEM TOTAL
  item_total = 0
#Print the grand total in dollar format
print("Grand Total: $%.2f" %grand_total)
