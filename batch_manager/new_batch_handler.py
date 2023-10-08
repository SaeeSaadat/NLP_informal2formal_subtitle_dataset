"""
In this new method, we're not gonna use the English data at all.
The main reason is that the persian translation is often very off and inaccurate so it doesn't match
the English translation. So we're gonna use the Persian data as the base and translate it to English, then
translate it back to persian to get our formal sentences.
"""
import os
import csv

from tqdm import tqdm

import config
from xlsxs import xlsx_writer, xlsx_reader
from cleanup import data_cleaner, purge_english
from alternatives.create_sample_dataset import create_sample_dataset


def prepare():
    with open('../resources/OpenSubtitles.en-fa.fa', 'r') as fa_file:
        persian_lines = fa_file.readlines()

    num_of_batches = len(persian_lines) // config.GOOGLE_TRANSLATE_BATCH_SIZE
    for i in range(num_of_batches + 1):
        print("\n\n Batch Number: \t", i)
        max_index = min(len(persian_lines) + 1, (i + 1) * config.GOOGLE_TRANSLATE_BATCH_SIZE)
        persian_subset = persian_lines[i * config.GOOGLE_TRANSLATE_BATCH_SIZE:max_index]

        persian_data = data_cleaner.prepare_lines_persian_only(persian_subset, True)
        xlsx_writer.write_to_sheet(persian_data, f'../xlsxs/NEW/informal/batch_{i}.xlsx')


def merge():
    num_of_files = len([name for name in os.listdir('../xlsxs/NEW/informal') if name.endswith('.xlsx')])
    with open('../resources/New-OpenSubtitle-Informal2Formal.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['informal', 'formal'])

        for i in tqdm(range(num_of_files)):
            informal_lines = xlsx_reader.read_from_xlsx(f'../xlsxs/NEW/informal/batch_{i}.xlsx', True)
            informal_lines = map(lambda x: x.replace('\n', ''), informal_lines)
            formal_lines = xlsx_reader.read_from_xlsx(f'../xlsxs/NEW/formal/batch_{i}.xlsx', True)

            writer.writerows([[original_line, translated_line] for original_line, translated_line in
                              zip(informal_lines, formal_lines)])


def prepare_degarbayan():
    with open('../resources/degarbayan_raw.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        data = [(row[0], row[1]) for row in reader if row[0] != 'informal']
        data = data_cleaner.prepare_persian_informal_formal_tuples(data, True)
        with open('../resources/degarbayan_processed.csv', 'w') as csv_output:
            writer = csv.writer(csv_output)
            writer.writerows(data)


def merge_all_datasets():
    """
    This function is used to merge all the datasets into one big dataset.
    :return:
    """
    dataset_files = [
        "../resources/handmade_dataset.csv",
        "../resources/New-OpenSubtitle-Informal2Formal.csv",
        "../resources/degarbayan_processed.csv"
    ]

    data = [('informal', 'formal')]
    for file in dataset_files:
        print("Working on " + file.split('/')[-1] + " dataset")
        with open(file, 'r') as csv_file:
            reader = csv.reader(csv_file)
            file_data = [(f[0], f[1]) for f in reader if f[0] != 'informal']
            data.extend(file_data)

    with open('../resources/full_dataset.csv', 'w', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(data)


def final_cleanup(input_file='../resources/full_dataset.csv', output_file='../resources/FullDataset-FinalCleanup.csv'):
    purge_english.purge_english_rows(input_file, output_file)


def get_sample(dataset_file: str, do_final_cleanup=False, sample_size=500):
    if do_final_cleanup:
        final_cleanup(dataset_file, dataset_file.replace('.csv', '_cleanedUp.csv'))
        create_sample_dataset(dataset_file.replace('.csv', '_cleanedUp.csv'), 99, sample_size)
    else:
        create_sample_dataset(dataset_file, 99, sample_size)


if __name__ == '__main__':
    prepare()
    merge()
    prepare_degarbayan()
    merge_all_datasets()
    final_cleanup()
    get_sample('../resources/FullDataset-FinalCleanup.csv', False, 500)
