import csv


def put_sentences_in_quotation(csv_file: str):
    # This method will put all the sentences in the csv file in quotation marks.
    first_row_flag = True
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        with open(f'{csv_file}-Quotation.csv', 'w', encoding='utf-8') as output_file:
            # writer = csv.writer(output_file)
            for row in reader:
                if first_row_flag:
                    first_row_flag = False
                    output_file.write(','.join(row) + '\n')
                    continue
                # writer.writerow([f'\"{row[0]}\"', f'{row[1]}'])
                output_file.write(f'\"{row[0]}\",\"{row[1]}\"\n')


if __name__ == '__main__':
    put_sentences_in_quotation('../resources/clean_dataset.csv')
