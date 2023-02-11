if __name__ == '__main__':
    with open('new.txt', 'w') as file:  # w=write
        file.write('First line in the new file\n')

    with open('new.txt') as file: # =read/r=read
        print(file.read())  # First line in the new file

    with open('new.txt', 'a') as file:  # a=append
        file.write('Second line in the new file\n')

    with open('new.txt') as f:
        print(f.read())
        # First line in the new file
        # Second line in the new file

    import csv

    with open('test.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['user_id', 'user_name', 'comments_qty'])
        writer.writerow([1234, 'mxln', 23])
        writer.writerow([1235, 'ismxln', 2])
