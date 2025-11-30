"""Find all word-pair palingrams in a dictionary file using recursion."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from utility.load_dictionary import load  # noqa: E402

SCRIPT_DIR = Path(__file__).parent

# Load dictionary of words
WORD_LIST = load(SCRIPT_DIR.parent / "word-lists/2of4brif.txt")

CHAR_MIN = 1


def main():
    """Palingrams main function."""
    word_set = set(WORD_LIST)
    palingrams = find_palingrams(word_set)
    palingrams_sorted = sorted(palingrams)

    print(f"\nNumber of palingrams = {len(palingrams_sorted)}\n")
    for first, second in palingrams_sorted:
        print(f"{first} {second}")


def find_palingrams(word_set):
    """Find palingrams by recursively processing word list."""
    words = list(word_set)
    return find_palingrams_recursive(words, 0, word_set, [])


def find_palingrams_recursive(words, index, word_set, results):
    """Recursively find palingrams starting from index.

    Args:
        words: List of words to process.
        index: Current word index.
        word_set: Set of valid words for membership testing.
        results: Accumulated palingram pairs.

    Returns:
        List of palingram tuples.
    """
    # Base case: processed all words
    if index >= len(words):
        return results

    word = words[index]
    end = len(word)

    if end >= CHAR_MIN:
        reverse_word = word[::-1]
        check_word_palingrams(word, reverse_word, word_set, results)

    # Recursive case: process next word
    return find_palingrams_recursive(words, index + 1, word_set, results)


def check_word_palingrams(word, reverse_word, word_set, results):
    """Recursively check all split positions for palingrams.

    Args:
        word: The word to check.
        reverse_word: The reversed word.
        word_set: Set of valid words.
        results: List to append found palingrams.
    """
    check_position_recursive(word, reverse_word, 0, word_set, results)


def check_position_recursive(word, reverse_word, i, word_set, results):
    """Check a single position and recurse to next.

    Args:
        word: The word to check.
        reverse_word: The reversed word.
        i: Current split position.
        word_set: Set of valid words.
        results: List to append found palingrams.
    """
    end = len(word)

    # Base case: checked all positions
    if i >= end:
        return

    rev_suffix = reverse_word[end - i :]
    rev_prefix = reverse_word[: end - i]

    # Case 1: word[i:] matches the front of reverse_word
    if word[i:] == rev_suffix and rev_suffix in word_set:
        results.append((word, rev_suffix))

    # Case 2: word[:i] matches the back of reverse_word
    if word[:i] == rev_suffix and rev_prefix in word_set:
        results.append((rev_prefix, word))

    # Recursive case: check next position
    check_position_recursive(word, reverse_word, i + 1, word_set, results)


if __name__ == "__main__":
    main()
