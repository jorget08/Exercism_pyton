def count_words(sentence):
    puntuacion = '! @ # $ % ^ & * ( ) _ / - + ? " > < | : ; , . [ ] { } \\'.split()
    d = {}

    for c in puntuacion:
        sentence = sentence.strip().lower().replace(c," ").replace("\n"," ").replace("\t", " ")

    sentence = sentence.split(" ")
    sentence = [i for i in sentence if i!= '']

    for i in range(0,len(sentence)):
        while sentence[i][0]==sentence[i][-1] and sentence[i][0]=="'":
            sentence[i] = sentence[i][1:-1]
    
    for c in sentence:
        d[c] = sentence.count(c)

    return d
