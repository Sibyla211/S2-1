edad1 = int(input("Ingrese la edad 1:"))
edad2 = int(input("Ingrese la edad 2:"))
edad3 = int(input("Ingrese la edad 3:"))
if edad1>edad2 and edad1>edad3:
    print("La edad mayor es "+str(edad1)+" años")
elif edad2>edad1 and edad2>edad3:
    print("La edad mayor es "+str(edad2)+" años")
elif edad3>edad1 and edad3>edad2:
    print("La edad mayor es "+str(edad3)+" años")