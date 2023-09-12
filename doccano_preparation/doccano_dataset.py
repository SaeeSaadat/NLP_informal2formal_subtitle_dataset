"""
This script will prepare files for doccaon annotation based on our alternative datasets.
"""
import csv
from random import shuffle


def prepare_doccano_dataset(alternatives_dataset_file: str):
    with open(alternatives_dataset_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        titles = next(reader)
        with open('../resources/doccano_dataset.csv', 'w', encoding='utf-8') as output_file:
            writer = csv.writer(output_file)
            writer.writerow(['text', 'label'])
            for row in reader:
                text = row[0] + '\n'
                for index, translation in enumerate(row[1:]):
                    text += f' {index + 1}- {translation}\n'
                writer.writerow([text, ''])


def shuffle_doccano_dataset(alternatives_dataset_file: str):
    """
    This method will shuffle the options on doccano_dataset.csv file!
    To reduce bias when selecting the superior version, we shouldn't be able to predict which option is which.
    So, We need to shuffle the options but still have the ability to decipher
    """
    with open(alternatives_dataset_file) as file:
        reader = csv.reader(file)
        next(reader)  # skip first row
        with open('../resources/doccano_dataset_shuffled.csv', 'w', encoding='utf-8') as output_file, open('../resources/shuffled_orders.csv', 'w', encoding='utf-8'):
            writer = csv.writer(output_file)
            writer.writerow(['text', 'label'])
            for row in reader:
                shuffled_orders = list(range(1, len(row)))


if __name__ == '__main__':
    prepare_doccano_dataset('../resources/alternatives.csv')
