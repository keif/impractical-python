"""Map letters from string into dictionary & print bar chart of frequency."""

import sys
from collections import Counter

# Note: text should be a short phrase for bars to fit in IDLE window
text = "Like the castle in its corner in a medieval game, I foresee terrible \
trouble and I stay here just the same."

# Normalize & filter to alphabetic only
normalized = [c.lower() for c in text if c.isalpha()]

freq = Counter(normalized)

print("\nYou may need to stretch console window if text wrapping occurs.\n")
print("text =", text, file=sys.stderr)
print()

# Alphabetical, consistent order
for letter in sorted(freq):
    bar = "#" * freq[letter]
    print(f"{letter}: {bar} ({freq[letter]})")
