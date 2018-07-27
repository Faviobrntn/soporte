a=[['','x','x','',''],
   ['','','','x' ,  ''],
   ['' ,'x','x','x',"salida"],
   ['' ,'' ,'','','']]

posicionIni=[0,0]
posicionUlt=[0,0]
bandera=0

def resolver_laberinto(laberinto,posicion,ultimaPosicion,bandera):
    while bandera!=1:
        #derecha
        if (posicion[1])<(len(laberinto[1])-1):
            if (posicion[1]+1)!= ultimaPosicion[1]:
                if laberinto[posicion[0]][posicion[1]+1]=='':
                    ultimaPosicion[0]=posicion[0]
                    ultimaPosicion[1]=posicion[1]
                    posicion=[posicion[0],posicion[1]+1]
                    print(posicion)
                    resolver_laberinto(laberinto,posicion,ultimaPosicion,bandera)
                elif (laberinto[posicion[0]][posicion[1]+1]=="salida"):
                    print("ganaste")
                    bandera=1


        #abajo
        if (posicion[0]) < (len(laberinto)-1):
            if (posicion[0]+1)!= ultimaPosicion[0]:
                if laberinto[posicion[0]+1][posicion[1]]=='':
                    ultimaPosicion[0]=posicion[0]
                    ultimaPosicion[1]=posicion[1]
                    posicion=[posicion[0]+1,posicion[1]]
                    print(posicion)
                    resolver_laberinto(laberinto,posicion,ultimaPosicion,bandera)
                elif (laberinto[posicion[0]+1][posicion[1]]=="salida"):
                    print("ganaste")
                    bandera=1

        #arriba
        if posicion[0]>0:
            if (posicion[0]-1)!= ultimaPosicion[0]:
               if laberinto[posicion[0]-1][posicion[1]] == '':
                   ultimaPosicion[0]=posicion[0]
                   ultimaPosicion[1]=posicion[1]
                   posicion=[posicion[0]-1,posicion[1]]
                   print(posicion)
                   resolver_laberinto(laberinto,posicion,ultimaPosicion,bandera)
               elif (laberinto[posicion[0]-1][posicion[1]]=="salida"):
                   print("ganaste")
                   bandera=1

        #izquierda
        if (posicion[1])>0:
            if (posicion[1]-1)!= ultimaPosicion[1]:
                if laberinto[posicion[0]][posicion[1]-1]=='':
                    ultimaPosicion[0]=posicion[0]
                    ultimaPosicion[1]=posicion[1]
                    posicion=[posicion[0],posicion[1]-1]
                    print(posicion)
                    resolver_laberinto(laberinto,posicion,ultimaPosicion,bandera)
                elif (laberinto[posicion[0]][posicion[1]-1]=="salida"):
                    print("ganaste")
                    bandera=1
        #encerrado abajo derecha y arriba
        if ((laberinto[posicion[0]+1][posicion[1]]=='x' or posicion[0]+1==len(laberinto)-1) and laberinto[posicion[0]][posicion[1]+1]=='x' and laberinto[posicion[0]-1][posicion[1]]=='x' ):
            if (posicion[1]-1) == ultimaPosicion[1]:
                 ultimaPosicion[0]=posicion[0]
                 ultimaPosicion[1]=posicion[1]
                 posicion=[posicion[0],posicion[1]-1]
                 print(posicion)
                 resolver_laberinto(laberinto,posicion,ultimaPosicion,bandera)

        #encerrado abajo derecha y izquierda
        if (laberinto[posicion[0]+1][posicion[1]]=='x' and laberinto[posicion[0]][posicion[1]+1]=='x' and laberinto[posicion[0]][posicion[1]-1]=='x'):
            if (posicion[0]-1) == ultimaPosicion[1]:
                 ultimaPosicion[0]=posicion[0]
                 ultimaPosicion[1]=posicion[1]
                 posicion=[posicion[0],posicion[1]-1]
                 print(posicion)
                 resolver_laberinto(laberinto,posicion,ultimaPosicion,bandera)

        #encerrado abajo izquierda y arriba
        if (laberinto[posicion[0]+1][posicion[1]]=='x' and laberinto[posicion[0]][posicion[1]-1]=='x' and laberinto[posicion[0]-1][posicion[1]]=='x'):
            if (posicion[1]+1) == ultimaPosicion[1]:
                 ultimaPosicion[0]=posicion[0]
                 ultimaPosicion[1]=posicion[1]
                 posicion=[posicion[0],posicion[1]-1]
                 print(posicion)
                 resolver_laberinto(laberinto,posicion,ultimaPosicion,bandera)

        #encerrado izquierda derecha y arriba
        if ((posicion[0]) < (len(laberinto)-1) and posicion[0]>0):
            if (laberinto[posicion[0]][posicion[1]-1]=='x' and laberinto[posicion[0]][posicion[1]+1]=='x' and laberinto[posicion[0]-1][posicion[1]]=='x'):
                if (posicion[0]+1) == ultimaPosicion[1]:
                    ultimaPosicion[0]=posicion[0]
                    ultimaPosicion[1]=posicion[1]
                    posicion=[posicion[0],posicion[1]-1]
                    print(posicion)
                    resolver_laberinto(laberinto,posicion,ultimaPosicion,bandera)





resolver_laberinto(a,posicionIni,posicionUlt,bandera)

