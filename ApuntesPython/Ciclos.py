
import random

vidas = 5

puntos = 0

#Si sale cero pierde una vida
# si se genera cualquier otro numero dentro un rago establecido, gana puntos.

while vidas!=0:

    num= random.randint(0,9)

    if num != 0:
        puntos+=1
        print("Tienes ", puntos," puntos")
    else:
        vidas-=1
        print("Te quedan", vidas ," vidas")    
