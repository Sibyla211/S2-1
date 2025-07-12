soles = int(input("Ingrese un número de soles: "))

if soles==1 or soles==2 or soles==5:
    print("Es moneda")
elif soles==10 or soles==20 or soles==50 or soles==100 or soles==200:
    lturistico = ""
    if soles==10:
        lturistico= "Machu Picchu"
    elif soles==20:
        lturistico= "Chan Chan"
    elif soles==50:
        lturistico= "Templo Chavin de Huantar"
    elif soles==100:
        lturistico= "Sitio Arqueológico del Gran Pajatén"
    elif soles==200:
        lturistico= "Ciudad Sagrada de Caral"
    print("Es un billete y su lugar turístico correspondiente es: " + lturistico)

else:
    print("La denominación no existe")