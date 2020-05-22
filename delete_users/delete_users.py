from csv import reader,writer

def delete_users(first,last):
    count = 0
    with open('users.csv') as csv_file:
        csv_reader = reader(csv_file)
        rows = list(csv_reader)
        for row in rows:
            if row[0] == first and row[1] == last:
                rows.remove(row)
                count += 1

    with open('users.csv','w') as csv_file:
        csv_writer = writer(csv_file)
        csv_writer.writerows(rows)


    return f'Users deleted: {count}.'
