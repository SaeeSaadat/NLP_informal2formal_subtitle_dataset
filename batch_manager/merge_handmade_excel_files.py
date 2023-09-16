"""
This project has gotten way too long! uhgh
"""
from xlsxs import xlsx_reader, xlsx_writer
import os
import csv
import datasets


def read_and_merge_all_files():
    # files_in_dir = xlsx_reader.get_all_files_in_dir('../resources/handmade_dataset/clean_sections')
    files_in_dir = os.listdir('../resources/handmade_dataset/clean_sections')
    data = [('informal', 'formal')]
    for file in files_in_dir:
        file_data = xlsx_reader.read_from_xlsx(f'../resources/handmade_dataset/clean_sections/{file}', False)
        file_data = [(f[0], f[1]) for f in file_data if f[0] is not None and f[1] is not None and len(f[0]) > 2]
        if file_data[0][0] in ['text', 'result', '', 'formal', 'رسمی', 'محاوره']:
            file_data = file_data[1:]
        data.extend(file_data)

    # Write excel file
    xlsx_writer.write_to_sheet(data, '../resources/handmade_dataset/cleaned_dataset.xlsx')

    # Write csv file
    with open('../resources/handmade_dataset.csv', 'w', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(data)


def push_csv_to_hub():
    dataset = datasets.load_dataset('csv', data_files='../resources/handmade_dataset.csv')
    dataset.push_to_hub("NVMSH/informal2formal_handmade_dataset")


if __name__ == '__main__':
    # read_and_merge_all_files()
    push_csv_to_hub()
