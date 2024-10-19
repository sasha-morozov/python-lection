input_str = input("Enter space-separated integers: ")
numbers = list(map(int, input_str.split()))
result_sum = sum(numbers)
print("The sum of the numbers is:", result_sum)
