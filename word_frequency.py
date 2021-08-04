STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    with open(file) as opened_file:
        raw_text = opened_file.read()

    raw_text = raw_text.lower().replace("\n", " ")
    punct = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for char in raw_text:
        if char in punct:
            raw_text = raw_text.replace(char, "")

    text_list = raw_text.split()
    text_list_copy = text_list.copy()
    word_count = {}

    for word in text_list_copy:
        if word in STOP_WORDS:
            text_list_copy.remove(word)
        elif word not in word_count:
            word_count[word] = text_list_copy.count(word)

    sorted_count = sorted(word_count.items(), key=lambda seq: seq[1], reverse=True)
    for x in sorted_count:
        print(x[0].rjust(20), ' | ', str(x[1]).center(3), (x[1]*("*")))


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
