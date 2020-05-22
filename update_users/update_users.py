from csv import reader,writer

def update_users(old_first,old_last,new_first,_new_last):
    count = 0
    with open('users.csv') as file:
        text = reader(file)
        rows = list(text)

    with open('users.csv','w') as file:
        csv_writer = writer(file)
        for row in rows:
            if row[0] == old_first and row[1] == old_last:
                csv_writer.writerow([new_first, _new_last])
                count += 1
            else:
                csv_writer.writerow(row)

    return f'Users updated: {count}.'

print(update_users("Grace", "Hopper", "Hello", "World"))
print(update_users("Colt", "Steele", "Boba", "Fett"))
