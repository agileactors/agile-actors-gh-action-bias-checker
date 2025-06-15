import re


def normalize_word(word):
    """
    Normalize a word by splitting it into parts based on:
    - underscores (_)
    - camelCase transitions
    - dots (.)
    - slashes (/)
    - question marks (?)
    - exclamation marks (!)
    - at symbols (@)
    - and removing digits from each part.
    :param word: The input word to normalize.
    :return: A list of cleaned lowercase components with digits removed.
    """
    parts = re.split(r'[_./?!@]|(?<=[a-z])(?=[A-Z])', word)
    cleaned = [
        stripped.lower()
        for p in parts
        if (stripped := re.sub(r'\d+', '', p))
    ]
    return cleaned
