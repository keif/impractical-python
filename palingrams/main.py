"""Find all word-pair palingrams in a dictionary file."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from utility.load_dictionary import load

SCRIPT_DIR = Path(__file__).parent

# Load dictionary of words
WORD_LIST = load(SCRIPT_DIR / "2of4brif.txt")

CHAR_MIN = 2


def main():
    """Palingrams main function."""
    palingrams = find_palingrams(WORD_LIST)
    # sort palingrams on first word
    palingrams_sorted = sorted(palingrams)

    # display list of palingrams
    print(f"\nNumber of palingrams = {len(palingrams_sorted)}\n")
    # Print word-pair palingrams from palingram list
    for first, second in palingrams_sorted:
        print(f"{first} {second}")


def find_palingrams(word_list):
    """Find palingrams in passed in word list."""
    word_set = set(word_list)  # speed up membership tests
    # Empty list to hold palingrams
    paligram_list = []

    for word in word_set:
        end = len(word)
        reverse_word = word[::-1]

        # skip single letters
        if end < CHAR_MIN:
            continue

        for i in range(end):
            # Case 1: word[i:] matches the front of reverse_word
            if (
                word[i:] == reverse_word[end - i :]
                and reverse_word[end - i :] in word_set
            ):
                paligram_list.append((word, reverse_word[end - i :]))

            # Case 2: word[:i] matches the back of reverse_word
            if (
                word[:i] == reverse_word[end - i :]
                and reverse_word[: end - i] in word_set
            ):
                paligram_list.append((reverse_word[: end - i], word))

    return paligram_list


if __name__ == "__main__":
    main()
