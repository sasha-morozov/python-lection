number = input("Provide 4-digit number: ")
if len(number) == 4 and number.isdigit():
    digits = [int(d) for d in number]
    total = sum(digits)

    print(f"{' + '.join(map(str, digits))} = {total}")
else:
    print("The number isn't 4-digit number.")
