from os import system
import time
import math
import csv
usug=51652 #Usuario
cong=["25615"] # Contraseña
e=652 #Primer dígito captcha
f=5*2-6+1 #Segundo dígito captcha
captcha=e+f   #Validación captcha
coord=[] #Ubicación de las coordenadas
regcoord={} #Diccionario de registro de coordenadas
def distancia(e1,f1,g1,h1): #Función para el cálculo de la distancia
    e2=(e1*math.pi)/180
    f2=(f1*math.pi)/180
    g2=(g1*math.pi)/180
    h2=(h1*math.pi)/180
    r=6372795.477598*2*math.asin(math.sqrt((math.sin((g2-e2)/2))**2+(math.cos(g2)*math.cos(e2)*(math.sin((h2-f2)/2))**2))) #Fórmula distancia
    return r
#Programa principal
print("¡Bienvenido! al sistema de ubicación para zonas públicas WIFI")
usu=int(input("Favor ingresar el Nombre de Usuario: "))
if usu==usug: #Verificación usuario
    cont=str(input("Ingrese la contraseña: "))
    if cont==cong[0]: #Verificación contraseña
        entcaptcha=int(input(f"El resultado de la suma {e} + {f} es: "))
        if entcaptcha==captcha: #Verificación captcha
            print("Sesión Iniciada")
            menu=["1Cambiar contraseña","2Ingresar coordenas actuales","3Ubicar zona WiFI más cercana","4Guardar archivo con ubicación cercana","5Actualizar registros de zonas wifi desde archivo","6Elegir opción de menú favorita","7Cerrar sesión"] 
            con=0 #Contador error
            while True:
                ubzonaswifi=[[0,10.348,-73.051,0],[0,10.171,-73.136,0],[0,10.259,-73.069,67],[0,10.350,-73.043,45]] #Matriz zonas wifi
                time.sleep(2) #Tiempo de espera
                system("cls") #Borra pantalla
                for i in range(len(menu)): #Muestra pantalla
                    print(f"{i+1}. {menu[i][1:]}")
                opc=int(input("Elija una opción: ")) #Selección de opción
                if opc<1 or opc>7: #Si no selecciona opción del menú
                    con=con+1
                    print("Error")
                    if con==3: #Contador
                        break
                else: 
                    opc2=int(menu[opc-1][0]) #Saca el primer valor de los string del menú
                    if opc2==1: #Cambio de contraseña
                        con=0 #Reinicio de contador
                        cont=str(input("Ingrese la contraseña actual: "))
                        if cont==cong[0]:
                            cont=str(input("Ingrese la nueva contraseña: "))
                            if cont==cong[0]:
                                print("No puede poner la misma contraseña")
                            else:
                                cong.append(cont) 
                                cong.pop(0)
                        else:
                            print("Error") #Si ingresa mal la contraseña actual
                            continue
                    elif opc2==2:
                        con=0
                        print("Ingreso de coordenadas actuales: \n1. Trabajo 2. Hogar 3. Parque ")
                        if len(coord)==3:
                            masnort=[]
                            masocc=[]
                            for i in range(3):
                                print(f"Coordenada [latitud, longitud] {i+1}: {coord[i]}")
                                masnort.append(coord[i][0])
                                masocc.append(coord[i][1])
                            print(f"La coordenada {masnort.index(max(masnort))+1} es la que está más al norte")
                            print(f"La coordenada {masocc.index(min(masocc))+1} es la que está más al occidente")
                            print("Presione 1,2 ó 3 para actualizar la respectiva coordenada. Presione 0 para regresar al menú")
                            selcoor=int(input())
                            if selcoor<0 or selcoor>3:
                                print("Error actualización")
                                continue
                            elif selcoor==0:
                                continue
                            else:
                                selcoor=selcoor-1
                                lat=float(input("Por favor ingrese la latitud: ")) #
                                if lat>10.462 or lat<9.757:
                                    print("Error coordenada")
                                    continue
                                else:
                                    long=float(input("Por favor ingrese la longitud: ")) #Ingreso longitud
                                    if long<-73.623 or long>-72.987:
                                        print("Error coordenada")
                                        continue
                                    else:
                                        coord[selcoor][0]=lat
                                        coord[selcoor][1]=long
                        else:
                            for i in range(3):
                                lat=float(input(f"Por favor ingrese la latitud {i+1}: ")) #Ingreso latitud
                                if lat>10.462 or lat<9.757:
                                    print("Error coordenada")
                                    continue
                                else:
                                    long=float(input(f"Por favor ingrese la longitud {i+1}: ")) #Ingreso longitud
                                    if long<-73.623 or long>-72.987:
                                        print("Error coordenada")
                                        continue
                                    else:                                        
                                        coord.append([lat,long])
                    elif opc2==3: #Zonas wifi cercanas
                        if len(coord)!=3: #Revisa si ya se han registrado las coordenadas más comúnes
                            print("Error sin registro de coordenadas")
                            quit()
                        else: #Cuando ya se registró
                            for i in range(3):
                                print(f"Coordenada [latitud, longitud] {i+1}: {coord[i]}")
                            selcoor=int(input("Por favor elija su ubicación actual (1,2 ó 3) para calcular la distancia a los puntos de conexión: "))
                            regcoord["actual"]=[f"Latitud: {coord[selcoor-1][0]}",f"Longitud: {coord[selcoor-1][1]}"] #Regitra ubicación actual
                            if selcoor<1 or selcoor>3:
                                print("Error ubicación") 
                                quit()  
                            else:
                                ar=[]
                                for i in range(len(ubzonaswifi)):
                                    dist=distancia(coord[selcoor-1][0],coord[selcoor-1][1],ubzonaswifi[i][1],ubzonaswifi[i][2]) #Cálculo de las distancias
                                    ubzonaswifi[i][0]=dist #Cambiar en primera columna por la distancia
                                ubzonaswifi.sort() #Reorganiza la lista dependiendo el primer elemento que es la distancia
                                for i in range(2):
                                    print(f"La zona wifi {i+1}: ubicada en [{ubzonaswifi[i][1]:.3f},{ubzonaswifi[i][2]:.3f}] a {ubzonaswifi[i][0]:.3f} metros, tiene en promedio {ubzonaswifi[i][3]:.0f} usuarios")
                                indlleg=int(input("Elija 1 o 2 para recibir indicaciones de llegada: "))
                                regcoord["zonawifi1"]=[f"Latitud: {ubzonaswifi[indlleg-1][1]}",f"Longitud: {ubzonaswifi[indlleg-1][2]}",f"Usuarios: {ubzonaswifi[indlleg-1][3]}"] #Registra zona más cercana
                                if indlleg==1 or indlleg==2:
                                    diflat=ubzonaswifi[indlleg-1][1]-coord[selcoor-1][0] #Para saber si se encuentra más al norte o al sur
                                    diflong=ubzonaswifi[indlleg-1][2]-coord[selcoor-1][1] #Para saber si se encuentra más al occidente o al oriente
                                    if diflat<0:
                                        sn="sur"
                                    else:
                                        sn="norte"
                                    if diflong>0:
                                        oo="oriente"
                                    else:
                                        oo="occidente"
                                    print(f"Para llegar a la zona wifi dirigirse primero al {oo} y luego hacia el {sn}")
                                    tb=(ubzonaswifi[indlleg-1][0]/16.67)*(1/60) #Cálculo tiempo de viaje en bus en minutos
                                    ta=(ubzonaswifi[indlleg-1][0]/20.83)*(1/60) #Cálculo tiempo de viaje en auto en minutos
                                    print(f"Tiempo de llegada en bus: {tb:.0f} minutos \nTiempo de llegada en auto: {ta:.0f} minutos")
                                    regcoord["recorrido"]=[f"{ubzonaswifi[indlleg-1][0]:3f} m",[f"Bus {tb:.0f} min",f"Auto {ta:.0f} min"]] #Registra llegada
                                else:
                                    print("Error zona wifi")
                                    quit()
                    elif opc2==4: #Guardar archivo con ubicación cercana
                            if len(regcoord)==3: #Verifica que haya registrado coordenadas y seleccione actual y como llegar
                                print(regcoord)
                                impr=int(input("¿Está de acuerdo con la información a exportar? Presione 1 para confirmar, 0 para regresar al menú principal\n"))
                                if impr==0:
                                    continue
                                elif impr==1:
                                    print("Exportando archivo")
                                    file=open("Registro de coordenadas.txt","a") #Crea archivo a para anexar infor
                                    texto="Registro de coordenadas \n" #Crea un título
                                    for i,j in regcoord.items(): #Añade toda la información del diccionario en lista
                                        texto=texto + f'{i},{j}\n'
                                    file.write(texto) #Lo escribe en el doc 
                                    file.close() #Cierra el archivo  
                                    quit()     
                            else:
                                print("Error de alistamiento")
                                quit()
                    elif opc2==5: #Actualizar zonas wifi desde archivo
                        #with open(r'C:\Users\fblum\Downloads\grupo1_5152.csv', newline='') as file:
                         #   doc=csv.reader(file)
                          #  doclis=[]
                           # for i in doc:
                            #    doclis.append(i)
                            #for i in range(len(ubzonaswifi)):
                             #   ubzonaswifi[i][1]=doclis[i+1][0]
                              #  ubzonaswifi[i][2]=doclis[i+1][1]
                               # ubzonaswifi[i][3]=doclis[i+1][2]
                        print("Datos de coordenadas para zonas wifi actualizados, presione 0 para regresar al menú principal")
                        selec=int(input())
                        if selec==0:
                            continue
                    elif opc2==6: #Selección de opción favorita
                        opcf=int(input("Elija la opción favorita: "))
                        if 5<opcf or opcf<1: #Si escoge un valor no disponible
                            print("Error")
                            continue        
                        else:
                            prueb1=int(input("Los tienes en las manos y los tienes en los pies y en seguida sabrás que número es.\nLa respuesta es: "))#Prubea 1 de seguridad
                            if prueb1==5:#Validación prueba 1
                                prueb2=int(input("Soy más de uno sin llegar a 3, y llego a 4 cuando me des dos.\nLa respuesta es: "))#Prueba 2 de seguridad
                                if prueb2==2: #Validación prueba 2
                                    aux=menu[opcf-1] #Auxiliar favorito
                                    menu.pop(opcf-1) #Borrar el valor favorito
                                    menu=[aux]+menu #Añade primero el favorito al menú
                                    print("Se hace el cambio")
                                else:
                                    print("Error")
                                    continue
                            else:
                                print("Error")
                                continue
                    elif opc2==7: #Salida del menú
                        print("Hasta pronto")
                        quit()
                    else: #Las opciones
                        con=0
                        print(f"Usted ha elegido la opción {opc}")
        else:
            print("Error") #Si falla en captcha
    else:
        print("Error") #Si falla en clave
else:
    print("Error") # Si falla usuario