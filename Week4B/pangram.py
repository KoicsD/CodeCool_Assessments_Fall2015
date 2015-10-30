__author__ = 'KoicsD'
# pangram task (deciding if a text contains all letters from the alphabet)


def is_pangram(text: str):
    alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    return all([(c in text.lower()) for c in alphabet])
