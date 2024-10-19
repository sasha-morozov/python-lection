# Виконайте переведення одиниць вимірювання відстаней. Значення відстані вказано у метрах. У
#кожному новому рядку програма виводить значення відстані, представлене у: дюймах, футах,
#милях, ярдах тощо. Числові дані на екрані мають бути у відформатованому вигляді: два знаки
#після десяткової крапки. Використайте функцію format(). Потрібні значення одиниць
#вимірювання знайдіть у мережі Інтернет.

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
