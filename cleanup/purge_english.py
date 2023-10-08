import csv
import re
from tqdm import tqdm
import datasets

english_regex = re.compile(r'[a-zA-Z]')


def contains_english_word(text):
    return bool(english_regex.search(text))


def count_rows_with_english_words(csv_file):
    all_rows, count = 0, 0
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in tqdm(reader):
            all_rows += 1
            if len(row) >= 2 and (contains_english_word(row[0]) or contains_english_word(row[1])):
                count += 1
    print("Number of rows with English words:", count, "\nout of total rows:", all_rows)
    return count, all_rows


def replace_english_digits_with_persian(text):
    return text.replace('0', '۰').replace('1', '۱').replace('2', '۲').replace('3', '۳').replace('4', '۴') \
        .replace('5', '۵').replace('6', '۶').replace('7', '۷').replace('8', '۸').replace('9', '۹')


def purge_english_rows(input_csv, output_csv):
    skipped_rows = 0
    all_rows_count = 0

    with (open(input_csv, 'r', encoding='utf-8') as input_file,
          open(output_csv, 'w', encoding='utf-8', newline='') as output_file):
        reader = csv.reader(input_file)
        writer = csv.writer(output_file)

        for row in reader:
            all_rows_count += 1
            if len(row) >= 2 and (contains_english_word(row[0]) or contains_english_word(row[1])):
                skipped_rows += 1
            else:
                writer.writerow((
                    replace_english_digits_with_persian(row[0]),
                    replace_english_digits_with_persian(row[1])
                ))
        print("--- Skipped rows:", skipped_rows, ' out of ', all_rows_count, ' ---')


def push_dataset_to_huggingface(csv_file: str):
    dataset = datasets.load_dataset('csv', data_files=csv_file)
    dataset.push_to_hub('NVMSH/extended_informal2formal_dataset_PersianCharsOnly')


if __name__ == '__main__':
    # purge_english_rows('resources/Extended-Informal2Formal.csv',
    #                    'resources/Extended-Informal2Formal-PersianOnly.csv')
    push_dataset_to_huggingface('resources/Extended-Informal2Formal-PersianOnly.csv')