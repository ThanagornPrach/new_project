import csv

with open('test_csv.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0 
    for row in csv_reader:
        if line_count == 0: 
            print(type(csv_reader))
            print(row)
            print(f'column name are {", ".join(row)}')
            #','.join(row) == name, department, birthday month
            line_count += 1
        else: 
            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')

    print(f'processed {line_count} lines.')