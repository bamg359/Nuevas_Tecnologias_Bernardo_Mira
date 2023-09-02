

#$paid = False

payment= int(input("Indique el valor a pagar: "))

goToPaid = int(input("Desea pagar? y=1 n=0"))
y=1
n=0
if goToPaid != 0:
    print("El valor a pagar es: " , str(payment))
    payService = int(input("desea agregar el servicio? (y= 1/n=0)"))
    payment = payment+(payment* 0.1)
    if payService == y:
        print("El valor a pagar es de:" + str(payment))
    print("Gracias por su visita")    
else:
    print("indique el producto a pedir")
