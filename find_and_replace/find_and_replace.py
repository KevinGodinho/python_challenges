def find_and_replace(file_name, word, replacement_word):
    with open(file_name, 'r') as file:
        text = file.read()

    text = text.replace(word, replacement_word)

    with open(file_name,'w') as file:
        file.write(text)
