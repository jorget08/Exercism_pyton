def abbreviate(words):
    acronimo = words[0]
    words = words.lower()
    todo = "qazwxscdevrfbtgyhnmjuiklop'"
    for i in range(len(words)):
        if words[i] not in todo:
            if words[i+1] in todo:
                acronimo += words[i+1]
    return acronimo.upper()
