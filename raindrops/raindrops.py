def convert(number):
    gota = ''
    if number % 3 == 0:
        gota += 'Pling'
        

    if number % 5 == 0:
        gota += 'Plang'
        

    if number % 7 == 0:
        gota += 'Plong'
        

    if number % 3 != 0 and number % 5!= 0 and number % 7 != 0:
        gota += str(number)
        
    return gota