def is_isogram(string):
    for letra in 'abcdefghijklmnñopqrstuvwxyz':
        contador = 0
        for x in string:
            if letra == x.lower():
                contador +=1
        if contador > 1:
            return False
    return True
