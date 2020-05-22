from csv import DictReader

# this is how you can read rows from a csv is a dict and access the contents

def print_users():
    with open('users.csv') as file:
        text = DictReader(file)
        for row in text:
            print('{} {}'.format(row['First Name'],row['Last Name']))

print_users()
