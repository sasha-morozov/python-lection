user_name = " Oleksandr "

def print_user_name(name):
    print(f"'{name}'")
    print(f"'{name.lstrip()}'")
    print(f"'{name.rstrip()}'")
    print(f"'{name.strip()}'")  

print_user_name(user_name)
