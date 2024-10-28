
morse = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
}

letter = input("Enter a letter: ").upper()
print("Morse code:", morse.get(letter, "Not found"))
