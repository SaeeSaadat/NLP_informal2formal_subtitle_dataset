from typing import List
import hazm
import re

import tqdm

import config

normalizer = hazm.normalizer.Normalizer()


def prepare_lines(persian_lines: List[str], english_lines: List[str], cleanup: bool = False):
    results = [], []
    current_line = '', ''
    for persian_line, english_line in zip(persian_lines, english_lines):
        if cleanup:
            persian_line, english_line = cleanup_line(persian_line, english_line)
        current_line = (
            current_line[0] + (' ' if current_line[0] else '') + persian_line,
            current_line[1] + (' ' if current_line[1] else '') + english_line
        )
        if len(current_line[0]) >= config.MIN_CHAR_THRESHOLD:
            results[0].append(current_line[0])
            results[1].append(current_line[1])
            current_line = '', ''
    return results


def prepare_lines_persian_only(persian_lines: List[str], cleanup: bool = False):
    results = []
    current_line = ''
    for row in tqdm.tqdm(persian_lines):
        lines = split_sentences_by_punkt(row)
        for persian_line in lines:
            if len(persian_line) < 2:
                continue
            if cleanup:
                persian_line = cleanup_line(persian_line, '')[0]
            current_line = current_line + (' ' if current_line else '') + persian_line
            if len(current_line) >= config.MIN_CHAR_THRESHOLD:
                results.append(current_line)
                current_line = ''
    return results


def prepare_persian_informal_formal_tuples(data: List[tuple], cleanup: bool = False):
    results = []
    for row in tqdm.tqdm(data):
        informal_splitted = split_sentences_by_punkt(row[0])
        formal_splitted = split_sentences_by_punkt(row[1])

        if len(informal_splitted) != len(formal_splitted):
            if cleanup:
                informal_line, formal_line = cleanup_line(row[0], row[1])
            else:
                informal_line, formal_line = row[0], row[1]
            results.append((informal_line, formal_line))

        else:
            for informal, formal in zip(informal_splitted, formal_splitted):
                if cleanup:
                    informal_line, _ = cleanup_line(informal, '')
                    formal_line, _ = cleanup_line(formal, '')
                else:
                    informal_line, formal_line = informal, formal
                results.append((informal_line, formal_line))
    return results


def cleanup_line(persian_line: str, english_line: str):
    if config.REMOVE_PARENTHESES:
        persian_line = remove_parentheses(persian_line)
        english_line = remove_parentheses(english_line)

    if config.REMOVE_EMOJIS:
        english_line = remove_emojis(english_line)
        persian_line = remove_emojis(persian_line)

    if config.NORMALIZE_PERSIAN:
        persian_line = normalizer.normalize(persian_line)

    if config.REMOVE_PUNCTUATION:
        persian_line = remove_punctuation(persian_line)
        english_line = remove_punctuation(english_line)

    elif config.REMOVE_EXTRA_PUNCTUATION:
        persian_line = remove_extra_punctuation(persian_line)
        english_line = remove_extra_punctuation(english_line)

    return persian_line, english_line


def remove_parentheses(text):
    pattern = r"\([^()]*\)"
    return re.sub(pattern, "", text)


def remove_punctuation(text):
    pattern = r"[^\w\s]"
    return re.sub(pattern, "", text)


def remove_extra_punctuation(text):
    if text.startswith('-'):
        text = text[1:]

    # multiple signs
    pattern = r"([^\w\s])\1+"
    text = re.sub(pattern, r"\1", text)

    # This weird pattern of . ? at the end of the sentence
    text = re.sub(r"\.\s*\?|\?\s*\.|\.\s*؟|؟\s*\.", "؟", text)

    return text


def remove_emojis(text):
    emojis = re.compile("["
                        u"\U0001F600-\U0001F64F"  # emoticons
                        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                        u"\U0001F680-\U0001F6FF"  # transport & map symbols
                        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                        u"\U00002500-\U00002BEF"  # chinese char
                        u"\U00002702-\U000027B0"
                        u"\U00002702-\U000027B0"
                        u"\U000024C2-\U0001F251"
                        u"\U0001f926-\U0001f937"
                        u"\U00010000-\U0010ffff"
                        u"\u2640-\u2642"
                        u"\u2600-\u2B55"
                        u"\u200d"
                        u"\u23cf"
                        u"\u23e9"
                        u"\u231a"
                        u"\ufe0f"  # dingbats
                        u"\u3030"
                        "]+", re.UNICODE)
    return re.sub(emojis, '', text)


def split_sentences_by_punkt(text: str):
    separators = r'\.{3}|\.|\,|\?|\n|؟|\!|؛|\n'
    indices = [match.end() for match in re.finditer(separators, text)]
    last_index = 0
    result = []
    for idx in indices:
        result.append(text[last_index:idx] if text[idx - 1] != '\n' else text[last_index:idx - 1])
        last_index = idx
    if last_index != len(text):
        result.append(text[last_index:])
    return result
