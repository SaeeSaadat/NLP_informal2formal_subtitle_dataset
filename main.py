import data_cleaner


def main():
    with open('resources/OpenSubtitles.en-fa.fa', 'r') as fa_file:
        persian_lines = fa_file.readlines()
    with open('resources/OpenSubtitles.en-fa.en', 'r') as en_file:
        english_lines = en_file.readlines()

    persian_subset = persian_lines[:1000]
    english_subset = english_lines[:1000]

    data = data_cleaner.prepare_lines(persian_subset, english_subset, True)
    for p, e in data:
        print(p, '\n    ', e, '\n-----------------------\n')



if __name__ == '__main__':
    main()
