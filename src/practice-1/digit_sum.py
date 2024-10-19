#Виконайте розкладання чотирицифрового цілого числа і виведіть на екран суму цифр у числі.
#Наприклад, якщо обрали число 6259, то програма повинна вивести на екран повідомлення: 6 +
#2 + 5 + 9 = 22. Використайте функцію format() для відображення результату або f-рядки.

number = input("Provide 4-digit number: ")
if len(number) == 4 and number.isdigit():
    digits = [int(d) for d in number]
    total = sum(digits)

    print(f"{' + '.join(map(str, digits))} = {total}")
else:
    print("The number isn't 4-digit number.")
