capital_letters = []
for x in range(65,91):
    capital_letters.append(chr(x))
print(capital_letters)

small_letters = []
for x in range(97,123):
    small_letters.append(chr(x))
print(small_letters)

special_char = [' ']

letters = { }

letters['uppercase'] = tuple(capital_letters)
letters['lowercase'] = tuple(small_letters)
letters['special character'] = tuple(special_char)
print(letters['special character'])

while True:
    person = input("Give the name and surname of the person you want to get information about: ")
    x = 0

    for letter in person:
        print(letter)

        if letter in letters['lowercase'] or letter in letters['uppercase'] or letter in letters['special character']:
            try:
                name = person.split(' ')[0]
                surname = person.split(' ')[1]
                x += 1
            except:
                print("You only entered one word: name or surname of the person.")
        else:
            print("Your text contains numbers or special characters. Enter the correct name.")
            break
    if x > 0:
        break



