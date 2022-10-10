# ENTRADAS =VARIABLES = REFERNECIAS DE MEMORIA

nivelAgua=int(input("digite el nivel del agua: "))

#PROCESO

if(nivelAgua>0 and nivelAgua <20):
#SALIDA
    print(f"el nivel del agua es {nivelAgua} y este es bajo ")
elif(nivelAgua>=20 and nivelAgua<400):
#SALIDA
    print(f"el nivel del agua es {nivelAgua} operando normalmente ")
elif(nivelAgua>=400):
#SALIDA    
    print(f"el nivel del agua es {nivelAgua} llamen a FICO y LUPE ")
else:
#SALIDA    
    print(f"el nivel del agua no es valido ")