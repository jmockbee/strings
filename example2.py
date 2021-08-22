from typing import Text


def parts_of(text):
    text = text * 3
    return text + str(len(text))


print(parts_of("random string of characters "))
