
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'i']


def filter_letter(letter):
    vowel = ['a','e','i', 'o', 'u']

    if letter in vowel:
        return True
    else:
        return False 


letterser1 = filter(filter_letter, letters)

# print(letterser1)

for let in letterser1:
    print(let)

