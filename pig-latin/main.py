"""Transform input text into pig latin."""

import sys


def main():
    """Main function to execute the pig latin conversion."""
    text = input("Enter text to convert to pig latin: ")

    while True:
        pig_latin_text = to_pig_latin(text)
        print()
        print(f"{pig_latin_text}", file=sys.stderr)

        try_again = input("\n\nTry again? (Press Enter else n to quit)\n ")
        if try_again.lower() == "n":
            break

    input("\nPress Enter to exit.")


def to_pig_latin(text: str) -> str:
    """Convert the given text to pig latin."""

    def convert_word(word: str) -> str:
        vowels = "aeiouAEIOU"
        if word[0] in vowels:
            return word + "way"

        for i, letter in enumerate(word):
            if letter in vowels:
                return word[i:] + word[:i] + "ay"
        return word + "ay"  # for words without vowels

    words = text.split()
    pig_latin_words = [convert_word(word) for word in words]
    return " ".join(pig_latin_words)


if __name__ == "__main__":
    main()
