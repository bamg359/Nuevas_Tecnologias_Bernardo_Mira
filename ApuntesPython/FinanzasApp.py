# La aplicacion debe permitir registrar ingresos y contar el saldo de estos.
# Debe permitir registrar egresos y mostrar el saldo.
# Si el egreso es mayor que el saldo no debe permitir el retiro y mostrará un mensaje de saldo insufiente.
# La aplicacion llevara registro de los movimientos indicando el numero de ingresos y de egresos.


saldo = 0
acumIngresos= 0
acumEgresos=0

isOn = int(input("Ingrese 1 para inicializar el servicio: "))

while isOn !=0:

    opc = int(input("1. Ingreso:\n 2. Egreso\n 3. Salir"))

    if opc == 1:
        ingreso = int(input("Registre el ingreso:"))

        saldo = saldo + ingreso

        print(f"Su saldo es ${saldo}")
        #print("saldo es : " + saldo)
        #print("saldo es:", saldo)
        acumIngresos+=1
        print(acumIngresos)
        #acumIngresos = acumIngresos +1
    elif opc==2:
        egreso = int(input("Registe el monto a retirar:"))  

        saldo = saldo - egreso

        if saldo < 0:
            print("Saldo insuficiente")
            saldo = saldo + egreso
            print(saldo)
            
        else:
            print(f"Su saldo es:${saldo}")
        acumEgresos+= 1
        print(acumEgresos)
    elif opc== 3:
        print("Salir") 
        isOn=0         
    else:
        print("Ingrese una opción valida")
