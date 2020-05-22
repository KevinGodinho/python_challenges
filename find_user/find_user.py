from csv import reader

# emaple of how enumerate works
# the commented out portion is my code, the rest is Colt's

def find_user(first,last):
    with open('users.csv') as file:
        text = reader(file)
        # i = 0
        for i,row in enumerate(text):
            if row == [first,last]:
                return i
        #     if row[0] != first and row[1] != last:
        #         i += 1
        #     if row[0] == first and row[1] == last:
        #         return i
        return '{} {} not found.'.format(first,last)

print(find_user('Colt','Steele'))
print(find_user("Alan", "Turing"))
print(find_user("Not", "Here"))
