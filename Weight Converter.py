unit = input("Is you temperature in Celcsius or Farenheit C or F?: " )
temp = float(input("Enter your temperature: "))

if unit == "C":
    temp = round((9 *temp)/5 + 32,1)
    print(F" Your temperature is {temp} Farenheit")
elif unit == "F":
    temp = round((temp - 32) * 5/9,1)
    print(F" Your temperature is {temp} Celcius")
else:
    print(f"Your unit {unit} is not valid")


