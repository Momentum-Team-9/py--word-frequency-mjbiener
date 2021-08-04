STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    word_count = {}
    with open(file) as opened_file:
        raw_text = opened_file.read()

        # '''prints raw text'''
        print(raw_text)

    raw_text = raw_text.lower().replace("\n", " ")
    punct = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for char in raw_text:
        if char in punct:
            raw_text = raw_text.replace(char, "")

    # '''prints lower cased text without line breaks or punctuation'''
    print(raw_text)

    text_list = raw_text.split()
    text_list_copy = text_list.copy()

    # '''prints text in list format'''
    print(text_list_copy)

    for word in text_list_copy:
        if word in STOP_WORDS:
            text_list_copy.remove(word)
        elif word not in word_count:
            unsorted_word_count = text_list_copy.count(word)
            word_count[word] = unsorted_word_count

    sorted_word_count = sorted(word_count.values(), reverse=True)
    sorted_dictionary = {}

    for idx in sorted_word_count:
        for kys in word_count.keys():
            if word_count[kys] == idx:
                sorted_dictionary[kys] = word_count[kys]
    for key, value in sorted_dictionary.items():
        print(key.rjust(20), ' | ', str(value).center(3), value * ("*"))



if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
