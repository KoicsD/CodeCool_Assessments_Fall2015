__author__ = 'KoicsD'


# Creating a function that takes a string as argument,
# counts the occurances of letters in alphabet
# and returns the result as a dictionary.
# Finally, trying this function.


def char_freq(text: str):
    d_counts = {}
    for c in text.lower():
        if c.isalpha():
            if c in d_counts.keys():
                d_counts[c] += 1
            else:
                d_counts[c] = 1
    return d_counts


if __name__ == "__main__":
    example = "ssfdf;gherogvqne"
    print("For: \"%s\"" % example)
    print("It returns:")
    print(str(char_freq(example)))