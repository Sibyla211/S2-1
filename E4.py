edad=int(input("Ingrese su edad: "))
if edad>=0 and edad<=17:
    print("S/ 15")
elif edad>=18 and edad<=30:
    print("S/ 25")
elif edad>=31 and edad<=45:
    print("S/ 30")
elif edad>=46:
    print("S/ 10")