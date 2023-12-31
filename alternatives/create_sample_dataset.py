"""
This script will select a 500 row sample of the entire dataset in order to be used for the alternative dataset.
Before running this script, the full dataset file needs to be created.
To create the full dataset, first run create_full_dataset.py script.
"""

import csv
import random

import tqdm


def count_lines_in_csv_file(file_path: str):
    with open(file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        return sum(1 for _ in reader)


def create_sample_dataset(full_dataset_file: str, rand_seed: int, sample_size: int = 500, output_file: str = None):
    num_of_lines = count_lines_in_csv_file(full_dataset_file)
    print("Dataset length: ", num_of_lines)

    numbers = random.sample(range(num_of_lines), sample_size)

    with open(full_dataset_file, 'r') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  # don't want the header!
        data = [('informal', 'formal')] + [row for i, row in enumerate(reader) if i in numbers]

    output_file_name = output_file if output_file else f'../resources/alternatives/{sample_size}_sample_{rand_seed}.csv'
    with open(output_file_name, 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(data)

    informal_output_name = output_file_name.replace('.csv', '_informal.csv')
    with open(informal_output_name, 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows([(row[0],) for row in data])


def create_sample_complement(full_dataset_file: str, sample_data: list, output_file: str = None):
    """
    This method will create full_dataset - sample_data
    """
    full_count, complement_count = 1, 0
    output_file_name = output_file if output_file else full_dataset_file.replace('.csv', '_sample_complement.csv')
    sample_set = set(sample_data)
    with open(full_dataset_file, 'r') as dataset_file:
        with open(output_file_name, 'w') as output_csv:
            reader = csv.reader(dataset_file)
            writer = csv.writer(output_csv)
            writer.writerow(next(reader))  # First row
            for row in tqdm.tqdm(reader):
                full_count += 1
                if tuple(row) not in sample_set:
                    writer.writerow(row)
                    complement_count += 1
    print(f"Full count: {full_count}, complement count: {complement_count}")


if __name__ == '__main__':
    # random_seeds = (94, 32, 12)
    # random_seeds = (94,)
    # for s in random_seeds:
    #     random.seed(s)
    #     create_sample_dataset('../resources/New-OpenSubtitle-Informal2Formal-PersianOnly.csv', s)
    print("no main")