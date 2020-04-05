import sys
'''
Section 1: Collect customer input
'''

## OBTAINING THE RENTAL CODE
#This portion has the user input what term they would 
#like to be billed under. The selected rate impacts
#allowable miles and overall cost.

rentalCode = input("(B)udget, (D)aily, or (W)eekly rental?\n")

## OBTAINING THE RENTAL PERIOD
#This section has the user input how long they would like
#to rent the vehicle. They can choose a number in weeks
#or in days and at their desired rate. B and D are combined
#because they both bill a daily rate later on.

if rentalCode == 'B' or rentalCode == 'D':
  rentalPeriod = input("Number of Days Rented:\n")
elif rentalCode == 'W':
  rentalPeriod = input("Number of Weeks Rented:\n")

## CONSTANTS FOR RENTAL CODES
#This section outlines the base charges to be applied
#all other charges are on top of the base charge

weeklyCharge = float(190.00)
dailyCharge = float(60.00)
budgetCharge = float(40.00)
mileCharge = float(0.00)
baseCharge = float (0.00)

## BASE CHARGES CALCULATED
#This section calculates the overall rate without any
#mile charges or extras as a base to be used later.

if rentalCode == 'B':
  baseCharge = float(budgetCharge) * float(rentalPeriod)
elif rentalCode == 'D':
  baseCharge = float(dailyCharge) * float(rentalPeriod)
elif rentalCode == 'W':
  baseCharge = float(weeklyCharge) * float(rentalPeriod)

## MILEAGE INFORMATION
#This section obtains mileage
#from the renter and assigns it to a variable. First is the
#starting miles and second is the ending. Used together
#to calculate the total miles.

odoStart = input("Starting Odometer Reading:\n")

odoEnd = input("Ending Odometer Reading:\n")

totalMiles = int(odoEnd) - int(odoStart)

## Calculating Charges based on Miles

## CODE B MILECHARGE
#Code B had a general mile charge of $0.25/mile which is
#calculated below

if rentalCode == 'B':
  mileCharge = float(totalMiles) * float(0.25)

## CODE D MILECHARGE
#This next section calculates the mileCharge for 
#rentalCode D. In D, the mileCharge only applies to
#miles over 100/day. When the average of the miles 
#divides to a daily total of 101+, then the mile charge
#applies to each mile over the 100. I calcuated this based 
#on the code below with a rate of $0.25/mile.
averageDayMiles = 0
extraMiles = 0
if rentalCode == 'D':
  averageDayMiles = float(totalMiles) // float(rentalPeriod)
  if averageDayMiles <= float(100):
    mileCharge = float(0.00)
  if averageDayMiles > (100):
    extraMiles = float(totalMiles) - (float(100) * float(rentalPeriod))
  if extraMiles > float(0.00):
    mileCharge = float(extraMiles) * float(0.25)


## CODE W MILECHARGE
#This final section for mile charges was for code W.
#The allowable mileage per week was 900. Anything over
#the 900 mark per week is billed at 100 * rentalPeriod
#so a 1000, 1-week rental would have a charge of $100
#added to the base charge for the overage in miles.
averageWeekMiles = 0

if rentalCode == 'W':
  averageWeekMiles = float(totalMiles) // float(rentalPeriod)
  if averageWeekMiles > int(900):
    mileCharge = float(rentalPeriod) * 100.00

## TOTAL DUE
#This section calcuates the total amount due for the 
#rental by adding together the baseCharge + the
#mileCharge. This makes the amount due as a toal.
  
amtDue = float(baseCharge) + float(mileCharge)


## RENTAL SUMMARY
#This section displays the rental summary. The summary
#includes the rentalCode, the rentalPeriod, the 
#odoStart, the odoEnd, the totalMiles, and the amtDue
#in the format %.2f to display dollars and cents.
#The format is based on the prompt.


print ('Rental Summary')
print ('Rental Code: ', rentalCode)
print ('Rental Period: ', rentalPeriod)
print ('Starting Odometer: ', odoStart)
print ('Ending Odometer: ', odoEnd)
print ('Miles Driven: ', totalMiles)
print ('Amount Due: ',"$%.2f" % amtDue)
