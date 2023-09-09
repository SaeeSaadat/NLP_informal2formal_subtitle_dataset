"""
This script will communicate with Farsiyar's API to get their
version of formal translation of an informal sentence.
It is used to create the doccano dataset for evaluation.
"""

import requests
import json
from dotenv import load_dotenv
import os
import csv
import tqdm


def call_farsiyar(text):
    if os.getenv('FARSIYAR_API_KEY') is None:
        load_dotenv()
    api_key = os.getenv('FARSIYAR_API_KEY')
    if api_key is None:
        raise Exception("Farsiyar API key is not defined in .env file.")

    base_url = "http://api.text-mining.ir/api/"
    url = base_url + "Token/GetToken"
    querystring = {"apikey": api_key}
    response = requests.request("GET", url, params=querystring)
    data = json.loads(response.text)
    token = data['token']

    url = base_url + "TextRefinement/FormalConverter"
    headers = {
        'Content-Type': "application/json",
        'Authorization': "Bearer " + token,
        'Cache-Control': "no-cache"
    }

    if not (text.startswith("\"") and text.endswith("\"")):
        text = f'"{text}"'
    response = requests.request("POST", url, data=text.encode("utf-8"), headers=headers)
    return response.text


def add_farsiyar_to_dataset(base_dataset: str, limit: int = None):
    cnt = 0
    first_row_flag = True
    with open(base_dataset, 'r', encoding='utf-8') as base_file:
        reader = csv.reader(base_file)
        with open('../resources/alternatives.csv', 'w', encoding='utf-8') as output_file:
            writer = csv.writer(output_file)
            for row in tqdm.tqdm(reader):
                if first_row_flag:
                    first_row_flag = False
                    writer.writerow(row + ['farsiyar'])
                    continue
                farsiyar = call_farsiyar(row[0])
                writer.writerow(row + [farsiyar])
                cnt += 1
                if cnt == limit:
                    return


if __name__ == '__main__':
    add_farsiyar_to_dataset('../resources/clean_dataset.csv', limit=10)
