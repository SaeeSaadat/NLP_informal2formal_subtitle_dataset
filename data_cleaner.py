from typing import List
import hazm
import re
import config

normalizer = hazm.normalizer.Normalizer()


def prepare_lines(persian_lines: List[str], english_lines: List[str], cleanup: bool = False):
    result = []
    current_line = '', ''
    for persian_line, english_line in zip(persian_lines, english_lines):
        current_line = (
            current_line[0] + (' ' if current_line[0] else '') + persian_line,
            current_line[1] + (' ' if current_line[1] else '') + english_line
        )
        if len(current_line[0]) >= config.MIN_CHAR_THRESHOLD:
            if cleanup:
                current_line = cleanup_line(*current_line)
            result.append(current_line)
            current_line = '', ''
    return result


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

    return persian_line, english_line


def remove_parentheses(text):
    pattern = r"\([^()]*\)"
    return re.sub(pattern, "", text)


def remove_punctuation(text):
    pattern = r"[^\w\s]"
    return re.sub(pattern, "", text)


def remove_extra_punctuation(text):
    pattern = r""


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
