__author__ = 'KoicsD'


# Write a function translate() that will translate a text into "rovarsprlket" (Swedish for "robber's language").
# That is, double every consonant and place an occurrence of "o" in between. For example, translate("this is fun")
# should return the string "tothohisos isos fofunon".


alphabet = "abcdefghijklmnopqrstuvwxyz"
vowels = "aeiou"
consonants = [l for l in alphabet if l not in vowels]


def translate(text: str):
    translation = ""
    for c in text:
        translation += c
        if c.lower() in consonants:
            if c.islower():
                translation += 'o' + c
            else:
                translation += 'O' + c
    return translation


if __name__ == '__main__':
    assert translate("this is fun") == "tothohisos isos fofunon"
