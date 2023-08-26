import data_cleaner
import config
import xlsx_writer
import tqdm


def main():
    with open('resources/OpenSubtitles.en-fa.fa', 'r') as fa_file:
        persian_lines = fa_file.readlines()
    with open('resources/OpenSubtitles.en-fa.en', 'r') as en_file:
        english_lines = en_file.readlines()

    num_of_batches = len(english_lines) // config.GOOGLE_TRANSLATE_BATCH_SIZE
    for i in tqdm.tqdm(range(num_of_batches + 1)):
        max_index = min(len(english_lines) + 1, (i+1) * config.GOOGLE_TRANSLATE_BATCH_SIZE)
        persian_subset = persian_lines[i*config.GOOGLE_TRANSLATE_BATCH_SIZE:max_index]
        english_subset = english_lines[i*config.GOOGLE_TRANSLATE_BATCH_SIZE:max_index]

        persian_data, english_data = data_cleaner.prepare_lines(persian_subset, english_subset, True)
        xlsx_writer.write_to_sheet(english_data, f'xlsxs/english/batch_{i}.xlsx')
        xlsx_writer.write_to_sheet(persian_data, f'xlsxs/persian/batch_{i}.xlsx')





if __name__ == '__main__':
    main()
