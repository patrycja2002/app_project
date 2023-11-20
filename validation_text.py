# number = [0,1,2,3,4,5,6,7,8,9]
#
# x=0
# while x <= 0:
#     name = input("Give the name of the person you want to get information about: ")
#     for num in number:
#         if str(num) in name:
#             print("Your text contains numbers. Enter the correct name.")


# isinstance()
# split(' ')[0] -> name
#  split(' ')[1] -> surename
#
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
print(letters)