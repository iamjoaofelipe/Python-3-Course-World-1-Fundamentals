# convert celsius to fahrenheit.

def convert_temperature(celsius):
    return (celsius * 9/5) + 32

celsius = float(input("Enter temperature in celsius: ")) 

fahrenheit = convert_temperature(celsius)

print("You entered:", celsius, "°C and this temperature is equal to:", fahrenheit, "°F")

