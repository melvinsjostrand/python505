def fix_text(text):
    text = text.replace(" ", "").lower()
    start = 0
    stop = len(text) - 1

    return pali(start,stop,text)


def pali(start, stop, text):
    if (stop - start) <= 1:
        return True
    if text[start] == text[stop]:
        return pali(start + 1, stop - 1, text)
    else:
        return False


print(fix_text("racecar"))