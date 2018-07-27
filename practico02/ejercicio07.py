from datetime import datetime
#fechaInicio 1/07
#fecha fin 30/06
#funcion fin y funcion semanas(recibe una fecha y devuelve la cantidad de semanas desde el inicio del periodo)
def inicio(fecha):
    if fecha.month<7:
        año=fecha.year-1
        return "01/07/"+str(año)
    elif fecha.month>=7:
        return "01/07/"+str(fecha.year)

def fin(fecha):
    if fecha.month<=6:
        return "30/06/"+str(fecha.year)
    elif fecha.month>6:
        return "30/06/"+str(fecha.year+1)

def semana(fecha):
    ini=datetime.strptime(inicio(fecha), '%d/%m/%Y')
    dias=abs((fecha)-(ini)).days
    return (round(dias/7))




fecha1=datetime.strptime("01/07/2016", '%d/%m/%Y')
fecha2=datetime.strptime("01/02/2016", '%d/%m/%Y')
fecha3=datetime.strptime("5/08/2016", '%d/%m/%Y')


assert inicio(fecha1)=="01/07/2016"
assert inicio(fecha2)=="01/07/2015"
#assert inicio(fecha2)!="01/07/2015"
assert fin(fecha1)=="30/06/2017"
assert fin(fecha2)=="30/06/2016"
assert semana(fecha3)==5
