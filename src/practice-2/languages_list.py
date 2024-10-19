# 1. Збережіть назви мов світу (Ukrainian, French, Bulgarian, Norwegian, Latvian або інші)
# у списку. Простежте за тим, щоб елементи у списку не зберігались в алфавітному порядку.
# Застосуйте функції sorted(), reverse(), sort() до списку. Виведіть список на екран до і
# після використання кожної із функцій.

languages = ['Ukrainian', 'French', 'Bulgarian', 'Norwegian', 'Latvian']

print("Original List:", languages)

sorted_languages = sorted(languages)
print("Sorted List (using sorted()):", sorted_languages)

languages.reverse()
print("List after reverse():", languages)

languages.sort()
print("List after sort():", languages)


