mes=input("Nombre del mes: ")

año=int(input("Ingrese el año de su nacimiento: "))

if mes=="Enero" or"Febrero" or "Marzo" or "Abril":
    if año%2==0:
        print("Su piedra preciosa es: Esmeralda")
    else:
        print("Su piedra preciosa es: Zafiro")

elif mes=="Mayo" or"Junio" or "Julio" or "Agosto":
    if año%2==0:
        print("Su piedra preciosa es: Rubí")
    else:
        print("Su piedra preciosa es: Topacio")

elif mes=="Setiembre" or"Octubre" or "Noviembre" or "Diciembre":
    if año%2==0:
        print("Su piedra preciosa es: Amatista")
    else:
        print("Su piedra preciosa es: Jade")

else:
    print("Error")