def is_pangram(sentence):
    sentence = str.lower(sentence)
    sentence = set(sentence)
    todo = [ x for x in sentence if ord(x) in range(ord('a'), ord('z')+1)]

    if len(todo) == 26:
        return True
    else:
       return False
