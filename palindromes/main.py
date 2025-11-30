"""Finding Palindromes."""

from pathlib import Path

from utility.load_dictionary import load

SCRIPT_DIR = Path(__file__).parent


def main():
    """Finding Palindromes.

    How do we find palindromes?
    Compare a word to itself sliced backward.
    word = nurses
    word[:] // nurses
    word[::-1] // sesrun
    word != word[::-1] // not a palindrome
    """
    word_list = load(SCRIPT_DIR / "words.txt")
    palindrome_list = []
    for word in word_list:
        if len(word) > 1 and word == word[::-1]:
            palindrome_list.append(word)

    print(f"\nNumber of palindromes found = {len(palindrome_list)}\n")
    print(*palindrome_list, sep="\n")


if __name__ == "__main__":
    main()
