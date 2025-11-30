"""Find all word-pair palingrams in a dictionary file (optimized)."""

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
    paligram_set = set()  # use set to avoid duplicates

    # precompute reversed words
    reversed_words = {word: word[::-1] for word in word_set}

    for word in word_set:
        end = len(word)

        # skip single letters
        if end < CHAR_MIN:
            continue

        reverse_word = reversed_words[word]

        # start at 1 to skip redundant checks
        for i in range(1, end):
            # cache slices to avoid redundant computation
            rev_suffix = reverse_word[end - i :]
            rev_prefix = reverse_word[: end - i]

            # Case 1: word[i:] matches the front of reverse_word
            if word[i:] == rev_suffix and rev_suffix in word_set:
                paligram_set.add((word, rev_suffix))

            # Case 2: word[:i] matches the back of reverse_word
            if word[:i] == rev_suffix and rev_prefix in word_set:
                paligram_set.add((rev_prefix, word))

    return list(paligram_set)


if __name__ == "__main__":
    main()
