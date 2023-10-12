import csv


def merge_samples():
    gpt_clean_file = open('../resources/sample_results/GPT2_clean_500_sample_informal_with_formal.csv')
    gpt_whole_file = open('../resources/sample_results/GPT2-1M-3epoch-clean_500_sample_informal_with_formal_gpt2.csv')
    t5_clean_file = open('../resources/sample_results/clean_500_sample_informal_with_formal_t5_3.csv')
    t5_whole_file = open(
        '../resources/sample_results/T5_1M_3epoch_clean_500_sample_informal_with_formal_clean_500_sample.csv'
    )
    farsiyar_file = open('../resources/sample_results/FarsiYar_500_sample.csv', 'r')
    chat_gpt_file = open('../resources/sample_results/ChatGPT_500_sample_informal_with_formals.csv')
    method_files = [
        gpt_clean_file,
        gpt_whole_file,
        t5_clean_file,
        t5_whole_file,
        farsiyar_file,
        chat_gpt_file
    ]
    method_readers = [csv.reader(file) for file in method_files]

    try:
        [next(reader) for reader in method_readers]
        with open('../resources/sample_results/merged_500_sample.csv', 'w', encoding='utf-8') as output_file:
            writer = csv.writer(output_file)
            writer.writerow(['informal', 'gpt_clean', 'gpt_whole', 't5_clean', 't5_whole', 'farsiyar', 'chat_gpt'])
            row_index = 1
            while True:
                try:
                    values = [next(reader) for reader in method_readers]

                    for i in range(1, len(method_readers)):
                        if values[0][0].strip() != values[i][0].strip():
                            raise Exception(f"there's a problem at row {row_index}!!!!!!!!!!")

                    writer.writerow([values[0][0], values[0][1]] + [v[1] for v in values[1:]])
                    row_index += 1
                except StopIteration:
                    break
        print(f"Dataset with {row_index-1} rows was created successfully")
    finally:
        for f in method_files:
            f.close()


if __name__ == '__main__':
    merge_samples()
