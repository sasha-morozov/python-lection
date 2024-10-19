# 2. На вхід програми подається один рядок з цілими числами. Числа розділені пропусками.
# Необхідно вивести суму цих чисел. Наприклад, якщо був введений рядок чисел 2 -1 9 6, то
# результатом роботи програми буде їх сума 16

input_str = input("Enter space-separated integers: ")
numbers = list(map(int, input_str.split()))
result_sum = sum(numbers)
print("The sum of the numbers is:", result_sum)
