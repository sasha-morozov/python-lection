# 5. Поміркуйте над тим, яку інформацію можна було б зберігати у списку. Наприклад, створіть
# список професій, видів спорту, членів родини, назви океанів тощо, а потім викличте кожну
# функцію для роботи зі списками, яка була згадана у цьому розділі, хоча б один раз.
def process_list(items, list_name):
    print(f"\nOriginal list of {list_name}: {items}")
    
    sorted_items = sorted(items)
    print(f"Sorted {list_name}:", sorted_items)
    
    items.reverse()
    print(f"Reversed {list_name}:", items)
    
    items.sort()
    print(f"Sorted {list_name} (in-place):", items)

professions = ['Doctor', 'Engineer', 'Teacher', 'Artist', 'Chef']
process_list(professions, "professions")

sports = ['Football', 'Basketball', 'Tennis', 'Swimming', 'Cycling']
process_list(sports, "sports")

family_members = ['Mother', 'Father', 'Brother', 'Sister', 'Grandmother']
process_list(family_members, "family members")

oceans = ['Pacific', 'Atlantic', 'Indian', 'Southern', 'Arctic']
process_list(oceans, "oceans")
