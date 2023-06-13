#!/usr/bin/python3
"""
text indentation
"""


def text_indentation(text):
    """text indentation"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    phrase = ""
    for element in text:
        if element in [".", "?", ":"]:
            phrase += element
            print(phrase.strip())
            print()
            phrase = ""
        else:
            phrase += element
    print(phrase.strip(), end="")
    