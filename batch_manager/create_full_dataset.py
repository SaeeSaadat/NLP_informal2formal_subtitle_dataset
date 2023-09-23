import csv


def read_and_merge_all_files():
    dataset_files = [
        "../resources/handmade_dataset.csv",
        "../resources/OpenSubtitles-Informal2Formal.csv",
        "../resources/degarbayan_raw.csv"
    ]

    data = [('informal', 'formal')]
    for file in dataset_files:
        print("Working on " + file.split('/')[-1] + "dataset")
        with open(file, 'r') as csv_file:
            reader = csv.reader(csv_file)
            file_data = [(f[0], f[1]) for f in reader if f[0] != 'informal']
            data.extend(file_data)

    with open('../resources/full_dataset.csv', 'w', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(data)


if __name__ == '__main__':
    read_and_merge_all_files()
