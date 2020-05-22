def vowel_count(text):
    new_text = text.lower()
    vowels = dict()

    for key in new_text:
        if key in 'aeiou':
            vowels[key] = 0

    for key in new_text:
        if key in 'aeiou':
            vowels[key] += 1

    return vowels


vowel_count('awesome') # {'a': 1, 'e': 2, 'o': 1}
vowel_count('Elie') # {'e': 2, 'i': 1}
vowel_count('Colt') # {'o': 1}


# Instructor's solution
# def vowel_count(string):
#     lower_s = string.lower()
#     return {letter: lower_s.count(letter) for letter in lower_s if letter in "aeiou"}
