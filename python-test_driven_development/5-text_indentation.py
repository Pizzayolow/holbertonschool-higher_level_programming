#!/usr/bin/python3
"""
text indentation
"""


def text_indentation(text):
    """text indentation"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    phrase = ""
    for element in range(len(text)):
        if text[element] in [".", "?", ":"]:
            phrase += text[element]
            print(phrase)
            phrase = ""
            print()
        else:
            if text[element] == " " and text[element - 1] in [".", "?", ":"]:
                phrase = ""
            else:
                phrase += text[element]
    print(phrase, end="")
