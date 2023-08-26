from datasets import load_dataset, concatenate_datasets


def add_clean_dataset():
    """
    This function is used to add the clean dataset to the original dataset.
    """
    dataset = load_dataset('csv', data_files='resources/OpenSubtitles-Informal2Formal.csv')
    clean_dataset = load_dataset('csv', data_files='resources/clean_dataset.csv')
    dataset = concatenate_datasets([clean_dataset['train'], dataset['train']])

    dataset.push_to_hub("NVMSH/opensubtitle_informal2formal_dataset")


if __name__ == '__main__':
    add_clean_dataset()
