def distance(strand_a, strand_b):
    respuesta = 0
    if len(strand_a) != len(strand_b):
        raise ValueError("ValueError")
    for i in range(len(strand_a)):
        if strand_a[i] != strand_b[i]:
            respuesta += 1
    return respuesta
