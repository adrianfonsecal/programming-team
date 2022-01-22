#Autor: David Leobardo Pérez Cruz
# Fecha: 21/01/22
# Descripción: Algoritmo para calcular la fecha más nueva
 

import datetime
año_actual = datetime.datetime.today().year
mes_actual=datetime.datetime.today().month
dia_actual=datetime.datetime.today().day


fecha1=[]
fecha2=[]

meses_31=[1, 3, 5, 7, 8, 10, 12]
meses_30=[2, 4, 6, 9, 11]

fecha_mayor=[]


#OBTENER Y VALIDAR LAS FECHAS
print("Ingrese el año de la fecha 1")
año1=int(input())
while año1>año_actual or año1<=0:
    print("Por favor introduzca un año menor o igual al actual y que sea mayor a 0")
    año1=int(input())
fecha1.append(año1)

print("Ingrese el mes de la fecha 1")  
mes1=int(input())
if año1==año_actual:
    while mes1>mes_actual:
        print("Por favor introduzca un mes menor o igual al actual")
        mes1=int(input())

while mes1>12 or mes1<=0:
    print("Por favor introduzca un mes menor o igual a 12 y que sea mayor a 0")
    mes1=int(input())
fecha1.append(mes1)

print("Ingrese el día de la fecha 1")
dia1=int(input())
if año1==año_actual and mes1==mes_actual:
    while dia1>dia_actual:
        print("Por favor introduzca un dia menor al actual")
        dia1=int(input())
if mes1 in meses_31:
        while dia1>31 or dia1<=0:
            print("Este mes puede tener máximo 31 días, ingrese uno")
            dia1=int(input())
else:
    while dia1>30 or dia1<=0:
        print("Este mes puede tener máximo 30 días, ingrese uno")
        dia1=int(input())


fecha1.append(dia1)




print("Ingrese el año de la fecha 2")
año2=int(input())
while año2>año_actual or año2<=0:
    print("Por favor introduzca un año menor o igual al actual y que sea mayor a 0")
    año2=int(input())
fecha2.append(año2)

print("Ingrese el mes de la fecha 2")  
mes2=int(input())
if año2==año_actual:
    while mes2>mes_actual:
        print("Por favor introduzca un mes menor o igual al actual")
        mes2=int(input())
while mes2>12 or mes2<=0:
    print("Por favor introduzca un mes menor o igual a 12 y que sea mayor a 0")
    mes2=int(input())
fecha2.append(mes2)

print("Ingrese el día de la fecha 2")
dia2=int(input())
if año2==año_actual and mes2==mes_actual:
    while dia2>dia_actual or dia2<=0:
        print("Por favor introduzca un dia menor al actual")
        dia2=int(input())
if mes2 in meses_31:
        while dia2>31 or dia2<=0:
            print("Este mes puede tener máximo 31 días, ingrese uno")
            dia2=int(input())
else:
    while dia2>30 or dia2<=0:
        print("Este mes puede tener máximo 30 días, ingrese uno")
        dia2=int(input())

fecha2.append(dia2)


#OBTENER LA FECHA MAYOR

if año1==año2:
    if mes1==mes2:
        if dia1==dia2:
            fecha_mayor="Ambas fechas son iguales"
        elif dia1>dia2:
            fecha_mayor=(dia1 , mes1, año1)
        else:
            fecha_mayor=(dia2 , mes2, año2)
    elif mes1>mes2:
        fecha_mayor=(dia1 , mes1, año1)
    else:
        fecha_mayor=(dia2 , mes2, año2)


elif año1>año2:
    fecha_mayor= (dia1 , mes1, año1)
else:
    fecha_mayor= (dia1 , mes1, año1)



print("La fecha mayor es: " , fecha_mayor)

    



    
    
    
    
