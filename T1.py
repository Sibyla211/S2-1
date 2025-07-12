mililitros=int(input("Ingrese la cantidad de mililitros de agua disponible: "))/1000

if mililitros%20==0:
    print("Alcanza para " + str(int(mililitros/20))+ " cajas de 20 litros")
elif mililitros%20>0:
    print("Alcanza para " + str(int(mililitros/20))+ " cajas de 20 litros y sobran " + str(int((mililitros*1000)%20))+" mililitros")
elif (mililitros/20)<1:
    print("Alcanza para 0 cajas de 20 litros")

if mililitros%7==0:
    print("Alcanza para " + str(int(mililitros/7))+ " bidones de 7 litros")
elif mililitros%7>0:
    print("Alcanza para " + str(int(mililitros/7))+ " bidones de 7 litros y sobran " + str(int((mililitros*1000)%7000))+" mililitros")
elif (mililitros/7)<1:
    print("Alcanza para 0 bidones de 7 litros")

if mililitros%2==0:
    print("Alcanza para " + str(int(mililitros/2))+ " botellas de 2 litros")
elif mililitros%2>0:
    print("Alcanza para " + str(int(mililitros/2))+ " botellas de 2 litros y sobran " + str(int((mililitros*1000)%2000))+" mililitros")
elif (mililitros/2)<1:
    print("Alcanza para 0 botellas de 2 litros")

if (mililitros*1000)%600==0:
    print("Alcanza para " + str(int(mililitros*1000/600))+ " botellas de 600 mililitros")
elif (mililitros*1000)%600>0:
    print("Alcanza para " + str(int(mililitros*1000/600))+ " botellas de 600 mililitros y sobran " + str(int((mililitros*1000)%600))+" mililitros")
elif (mililitros*1000/600)<1:
    print("Alcanza para 0 botellas de 600 mililitros")