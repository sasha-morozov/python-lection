# This code is designed for distance conversion from meters to other units
meters = float(input("Введіть відстань у метрах: "))
inches = meters * 39.3701
feet = meters * 3.28084
miles = meters * 0.000621371
yards = meters * 1.09361

print("in inches: {:.2f}".format(inches))
print("in feet: {:.2f}".format(feet))
print("in miles: {:.2f}".format(miles))
print("in yards: {:.2f}".format(yards))
