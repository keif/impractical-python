"""Map letters from string into dictionary & print bar chart of frequency."""

import sys
from collections import Counter

# Note: text should be a short phrase for bars to fit in IDLE window
default_text = "Like the castle in its corner in a medieval game, I foresee terrible \
trouble and I stay here just the same."


def main():
    """Main function to convert string to a bar chart of frequency."""
    text = input("Enter a string: ")
    if len(text) == 0:
        print("Using default text.")
        text = default_text

    print("\nYou may need to stretch console window if text wrapping occurs.\n")
    print("text =", text, file=sys.stderr)
    print()

    convert_text(text)


def convert_text(text: str) -> None:
    """Convert string to dictionary and return bar chart of frequency."""
    # Normalize & filter to alphabetic only
    normalized = [c.lower() for c in text if c.isalpha()]

    freq = Counter(normalized)

    # Alphabetical, consistent order
    for letter in sorted(freq):
        bar = "#" * freq[letter]
        print(f"{letter}: {bar} ({freq[letter]})")


if __name__ == "__main__":
    main()
