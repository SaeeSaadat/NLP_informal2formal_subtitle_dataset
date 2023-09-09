"""
This script will prepare files for doccaon annotation based on our alternative datasets.
"""
import csv


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


if __name__ == '__main__':
    prepare_doccano_dataset('../resources/alternatives.csv')
