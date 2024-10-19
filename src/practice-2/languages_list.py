languages = ['Ukrainian', 'French', 'Bulgarian', 'Norwegian', 'Latvian']

print("Original List:", languages)

sorted_languages = sorted(languages)
print("Sorted List (using sorted()):", sorted_languages)

languages.reverse()
print("List after reverse():", languages)

languages.sort()
print("List after sort():", languages)
