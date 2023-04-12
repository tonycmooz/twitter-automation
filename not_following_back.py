import csv

def read_csv_single_values(file_name):
    with open(file_name, newline='') as csvfile:
        reader = csv.reader(csvfile)
        return [row[0] for row in reader]

def read_csv_multiple_values(file_name):
    with open(file_name, newline='') as csvfile:
        reader = csv.reader(csvfile)
        return [row for row in reader]

def write_filtered_rows_to_csv(file_name, filtered_rows):
    with open(file_name, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(filtered_rows)

def main():
    friends_list = 'twitter_friends.csv'
    friends = read_csv_single_values(friends_list)

    following_list = '11April_anthonymooz_following.csv'
    multiple_values = read_csv_multiple_values(following_list)

    filtered_rows = [row for row in multiple_values if row[0] not in friends]

    write_filtered_rows_to_csv('not_following_back.csv', filtered_rows)

if __name__ == '__main__':
    main()
