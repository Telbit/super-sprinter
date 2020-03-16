import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['', 'planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story():
    file = open('test_csv.csv', 'r')
    return [row for row in csv.DictReader(file)]


def write_data(new_data):
    f = open('test_csv.csv', 'w')
    headers = csv.OrderedDict()
    for key in DATA_HEADER:
        headers[key] = key
    new_data.insert(0, headers)
    fieldnames = DATA_HEADER
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    for i in new_data:
        writer.writerow(i)

