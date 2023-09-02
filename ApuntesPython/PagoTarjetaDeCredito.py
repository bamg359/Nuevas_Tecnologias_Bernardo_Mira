

# reciban por consola el valor de una compra
# que puedan ingresar el numero de coutas
# Calcular el valor de la cuota
# usando while queremos que imprima el plan de pago y le muestre el cupo liberado con cada pago

valorcompra = float(input("Ingrese el valor de compra: "))
numcuotas = int(input("Ingrese numero de cuotas: "))
valorcuota = valorcompra / numcuotas
cuota_actual = 1
saldo_restante = valorcompra
while cuota_actual <= numcuotas:
    print(f"Cuota {cuota_actual}: Valor de cuota = {valorcuota:.2f} | Saldo restante = {saldo_restante:.2f}")
    cuota_actual += 1
    saldo_restante -= valorcuota