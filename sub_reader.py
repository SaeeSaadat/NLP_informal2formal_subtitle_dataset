import data_cleaner


def main():
    persian_lines, english_lines = None, None
    with open('resources/OpenSubtitles.en-fa.fa', 'r') as fa_file:
        persian_lines = fa_file.readlines()
    with open('resources/OpenSubtitles.en-fa.en', 'r') as en_file:
        english_lines = en_file.readlines()


if __name__ == '__main__':
    main()
