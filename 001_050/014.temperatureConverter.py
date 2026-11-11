
# Celsius to Fahrenheit Converter

# Create a function to convert the temperature.
def convert_temperature(celsius):
    return (celsius * 9/5) + 32

# Get the temperature in Celsius.
celsius = float(input("Enter the temperature in Celsius: "))

# Convert Celsius to Fahrenheit.
fahrenheit = convert_temperature(celsius)

# Show the result.
print("You entered:", celsius, "°C and this temperature is equal to:", fahrenheit, "°F")
