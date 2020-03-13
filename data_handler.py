import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story():
    f = open(DATA_FILE_PATH)
    reader = csv.DictReader(f)
    return [row for row in reader]


# if __name__ == '__main__':
#     print(get_all_user_story())
