import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story():
    f = open('test_csv.csv', 'r')
    return csv.DictReader(f)


def write_data(a):
    f = open('test_csv.csv', 'w')
    fieldnames = ['a', 'b', 'c', 'd', 'e']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    a = [{'a': 1, 'b': 2, 'c': 3, 'd': "dsjv jdhv jdh vj ,dcfsvsve", 'e': a}]
    writer.writerow(a[0])


if __name__ == '__main__':
    # print(get_all_user_story()[0])
    write_data()
