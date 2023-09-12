import os
import csv
import datasets
from tqdm import tqdm
from xlsxs import xlsx_reader


def merger():
    """
    This function is used to merge the translated and original batches and create a huggingface dataset from it.

    """
    num_of_files = len([name for name in os.listdir('../xlsxs/translated') if name.endswith('.xlsx')])
    with open('../resources/OpenSubtitles-Informal2Formal.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['informal', 'formal'])

        for i in tqdm(range(num_of_files)):
            original_lines = xlsx_reader.read_from_xlsx(f'xlsxs/persian/batch_{i}.xlsx', True)
            translated_lines = xlsx_reader.read_from_xlsx(f'xlsxs/translated/batch_{i}.xlsx', True)
            original_lines = map(lambda x: x.replace('\n', ''), original_lines)

            writer.writerows([[original_line, translated_line] for original_line, translated_line in
                              zip(original_lines, translated_lines)])


def create_dataset():
    return datasets.load_dataset('csv', data_files='resources/OpenSubtitles-Informal2Formal.csv')


if __name__ == '__main__':
    merger()
    dataset = create_dataset()
    dataset.push_to_hub("NVMSH/opensubtitle_informal2formal_dataset")
