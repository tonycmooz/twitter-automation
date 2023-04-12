import csv

def read_csv_first_column(file_name):
    with open(file_name, newline='') as csvfile:
        reader = csv.reader(csvfile)
        return [row[0] for row in reader]

def find_friends(file_name, common_values):
    with open(file_name, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for value in common_values:
            writer.writerow([value])

def main():
    file1_values = read_csv_first_column('11April_anthonymooz_followers.csv')
    file2_values = read_csv_first_column('11April_anthonymooz_following.csv')

    common_values = set(file1_values) & set(file2_values)

    find_friends('twitter_friends.csv', common_values)

if __name__ == '__main__':
    main()
