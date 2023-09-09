"""
This script will create a dataset showing alternative versions of the formal translation from our informal sentences.
The result will feature the following columns:
    - informal: The informal sentence
    - formal: The formal sentence from our dataset
    - farsiyar: The formal sentence from Farsiyar's API
    - TODO: Add other alts
"""

import csv
from alternatives.farsiyar import add_farsiyar_to_dataset


def create_alts_dataset(base_dataset: str, limit: int = None):
    add_farsiyar_to_dataset(base_dataset, limit)


if __name__ == '__main__':
    create_alts_dataset('../resources/clean_dataset.csv', 100)
