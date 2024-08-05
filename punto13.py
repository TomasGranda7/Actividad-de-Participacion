def palindromo ():
    word = input ("Ingresa una palabra:")
    invertido = word [::-1]
    if word == invertido:
        print (word, "es un palindromo")
    else:
        print (word, "no es un palindromo")


palindromo ()