def factorial ():
    num = int(input("Ingresar numero:"))
    factorial = 1
    for i in range (num):
        
        factorial *=  i + 1
    print (factorial)

factorial ()