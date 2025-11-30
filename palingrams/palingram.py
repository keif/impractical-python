"""Find all word-pair palingrams in a dictionary file."""

from utility.load_dictionary import load

word_list = load("../word-lists/2of4brif.txt")


# find word-pair palingrams
def find_palingrams():
    """Find dictionary palingrams."""
    pali_list = []
    for word in word_list:
        end = len(word)
        rev_word = word[::-1]
        if end > 1:
            for i in range(end):
                if word[i:] == rev_word[: end - i] and rev_word[end - i :] in word_list:
                    pali_list.append((word, rev_word[end - i :]))
                if word[:i] == rev_word[end - i :] and rev_word[: end - i] in word_list:
                    pali_list.append((rev_word[: end - i], word))
    return pali_list


palingrams = find_palingrams()

# sort palingrams on first word
palingrams_sorted = sorted(palingrams)

# display list of palingrams
print(f"\nNumber of palingrams = {len(palingrams_sorted)}\n")
for first, second in palingrams_sorted:
    print(f"{first} {second}")
