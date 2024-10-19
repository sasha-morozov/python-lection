# This code is designed from temperature conversions

celsius = float(input("Provide temperature in celsius: "))
fahrenheit = 32 + (9/5) * celsius
kelvin = celsius + 273.15

print(f"In Fahrenheit: {fahrenheit:^15.2f}")
print(f"In kelvin: {kelvin:^15.2f}")
