"""
This script will select a 500 row sample of the entire dataset in order to be used for the alternative dataset.
Before running this script, the full dataset file needs to be created.
To create the full dataset, first run create_full_dataset.py script.
"""

import csv
import random


def count_lines_in_csv_file(file_path: str):
    with open(file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        return sum(1 for _ in reader)


def create_sample_dataset(full_dataset_file: str, rand_seed: int, sample_size: int = 500):
    num_of_lines = count_lines_in_csv_file(full_dataset_file)
    print("Dataset length: ", num_of_lines)

    numbers = random.sample(range(num_of_lines), sample_size)

    with open('../resources/full_dataset.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  # don't want the header!
        data = [('informal', 'formal')] + [row for i, row in enumerate(reader) if i in numbers]

    with open(f'../resources/alternatives/500_sample_raw_{rand_seed}.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(data)

    with open(f'../resources/alternatives/500_sample_informals_{rand_seed}.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows([(row[0],) for row in data])


if __name__ == '__main__':
    random_seeds = (94, 32, 12)
    for s in random_seeds:
        random.seed(s)
        create_sample_dataset('../resources/full_dataset.csv', s)
