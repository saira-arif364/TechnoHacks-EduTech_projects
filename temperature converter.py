 # 2 TASK

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius
def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit
def convert_temperature():
    conversion_type = input("Enter conversion type (1 for Fahrenheit to Celsius, 2 for Celsius to Fahrenheit): ")

    if conversion_type == "1":
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F is equal to {celsius}°C")

    elif conversion_type == "2":
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C is equal to {fahrenheit}°F")

    else:
        print("Invalid conversion type.")
convert_temperature()
def convert_temperature(temperature, unit):
    if unit == "F":
        celsius = (temperature - 32) * 5/9
        return celsius
    elif unit == "C":
        fahrenheit = (temperature * 9/5) + 32
        return fahrenheit
    else:
        return "Invalid unit"

# Prompt the user to enter a temperature and unit
temperature = float(input("Enter the temperature: "))
unit = input("Enter the unit (F/C): ")

# Call the convert_temperature function and display the converted temperature
converted_temperature = convert_temperature(temperature, unit)
print("The converted temperature is:", converted_temperature)
def convert_temperature(temp, unit):
    if unit.lower() == 'f':
        celsius = (temp - 32) * 5/9
        return celsius
    elif unit.lower() == 'c':
        fahrenheit = (temp * 9/5) + 32
        return fahrenheit
    else:
        return "Invalid unit of measurement"

