# 4. Необхідно зчитати рядок з 5 цифр, розділених пропусками, і зберегти кожну цифру у список.
# Створіть копію списку із впорядкованими елементами у зворотному порядку. Виведіть число,
# яке утворюється об’єднанням елементів нового списку.
input_string = input("Enter a string of 5 digits separated by spaces: ")
digits = input_string.split()
if len(digits) != 5 or not all(digit.isdigit() for digit in digits):
    print("Error: You must enter exactly 5 digits separated by spaces.")
else:
    reversed_digits = digits[::-1]
    reversed_number = ''.join(reversed_digits)
    print("Reversed number:", reversed_number)
