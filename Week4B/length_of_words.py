__author__ = 'KoicsD'
# mapping a list of words into a list of ints that indicates the length of the words


def length_of_words(words: list):
    if type(words) == str or any([type(item) != str for item in words]):
        raise TypeError()

    ret = []
    for word in words:
        ret.append(len(word))
    return ret
