import csv
import sys


try:
     num1 = float((input("Enter your height in m: "))) # Enter your height (m)
     assert num1 > 0 # Continue if the input value is a non-negative or non-zero
except AssertionError:
         print("You must not enter a negative value or a zero value!") # Error message if the input value is zero or negative
         sys.exit(1) # Exit the program
except ValueError: # If the input is a string
    print("You must enter a number!") # Error message if the input is a string
    sys.exit(1) # Exit the program

try:
    num2 = float(input("Enter your weight in kg: ")) # Enter your weight (kg)
    assert num2 > 0 # Continue if the input value is a non-negative or non-zero
except AssertionError:
    print("You must not enter a negative value or a zero value!") # Error message if the input value is zero or negative
    sys.exit(1) # Exit the program
except ValueError:  # If the input is a string
    print("You must enter a number!") # Error message if the input is a string
    sys.exit(1) # Exit the program


BMI = float(num2) /(float(num1) ** 2)   #Calculates the BMI


if BMI < 15:    # If the BMI is below 15
    print("Your are very severely underweight")
    newWeight = float(num2) * 18.6/BMI  # Calculates the recommended weight
    print(f"You need to weight {newWeight:.2f} kg to be healthy")
    gainWeight = float(newWeight) - float(num2) # Calculates the weight needed to be healthy
    print(f"and you need to gain {gainWeight:.2f} kg in weight to be healthy")


if 15 <= BMI < 16:  # If the BMI is between the intervals 15 and 16
    print("Your are severely underweight")
    newWeight = float(num2) * 18.6 / BMI # Calculates the recommended weight
    print(f"You need to weight {newWeight:.2f} kg to be healthy")
    gainWeight = float(newWeight) - float(num2) # Calculates the weight needed to be healthy
    print(f"and you need to gain {gainWeight:.2f} kg in weight to be healthy")
if 16 <= BMI < 18.5: # If the BMI is between the intervals 16 and 18.5
    print("Your are underweight")
    newWeight = float(num2) * 18.6 / BMI # Calculates the recommended weight
    print(f"You need to weight {newWeight:.2f} kg to be healthy")
    gainWeight = float(newWeight) - float(num2) # Calculates the weight needed to be healthy
    print(f"and you need to gain {gainWeight:.2f} kg in weight to be healthy")
if 18.5 <=BMI < 25: # If the BMI is between the intervals 18.5 and 25
    print("Your normal weight")
if 25 <= BMI < 30: # If the BMI is between the intervals 25 and 30
    print("Your overweight")
    newWeight = float(num2) * 24.9 / BMI # Calculates the recommended weight
    print(f"You need to weight {newWeight:.2f} kg to be healthy")
    loseWeight = -(float(newWeight) - float(num2))  # Calculates the weight needed to be healthy
    print(f"and you need to lose {loseWeight:.2f} kg in weight to be healthy")
if 30 <= BMI < 35: # If the BMI is between the intervals 30 and 35
    print("Your moderate obese")
    newWeight = float(num2) * 24.9 / BMI # Calculates the recommended weight
    print(f"You need to weight {newWeight:.2f} kg to be healthy")
    loseWeight = -(float(newWeight) - float(num2)) # Calculates the weight needed to be healthy
    print(f"and you need to lose {loseWeight:.2f} kg in weight to be healthy")
if 35 <= BMI < 40: # If the BMI is # If the BMI is between the intervals 35 and 40
    print("Your severe obese")
    newWeight = float(num2) * 24.9 / BMI # Calculates the recommended weight
    print(f"You need to weight {newWeight:.2f} kg to be healthy")
    loseWeight = -(float(newWeight) - float(num2)) # Calculates the weight needed to be healthy
    print(f"and you need to lose {loseWeight:.2f} kg in weight to be healthy")
if BMI >= 40: # If the BMI is above 40
    print("Your are very severely obese")
    newWeight = float(num2) * 24.9 / BMI # Calculates the recommended weight
    print(f"You need to weight {newWeight:.2f} kg to be healthy")
    loseWeight = -(float(newWeight) - float(num2))  # Calculates the weight needed to be healthy
    print(f"and you need to lose {loseWeight:.2f} kg in weight to be healthy")


data = [str(round(BMI, 2)),num2] # The data array
with open('BMI_and_Height.csv','a',newline='') as file: # Enters the data into the csv file
    writer = csv.writer(file, delimiter=",") # Write the data to the file
    writer.writerow(data) # Write the data to the rows

print("Your BMI is %.2f" % BMI) # Prints out the BMI






