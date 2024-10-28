languages = {
    'Python': 'Guido van Rossum',
    'Java': 'James Gosling',
    'C++': 'Bjarne Stroustrup',
    'JavaScript': 'Brendan Eich'
};

for language, creator in languages.items():
    print(f"My favorite programming language is {language}. It was created by {creator}.")

del languages['Java']

print(languages);
