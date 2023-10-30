def ultima_aparicion(s: list, e: int) -> int:
    if pertenece(s, e):
        for i in range(len(s)-1,-1,-1):
            if (s[i] == e):
                return i
    
def pertenece(s:list, e:int) -> bool:
    res: bool = False
    
    for i in range(0,len(s),1):
        if (s[i] == e):
            res = True
    return res 







def elementos_exclusivos(s:list, t:list) -> list:
    elementos_exc = []

    for i in s:
        if i not in t:
            elementos_exc.append(i)
    for j in t:
        if j not in s:
            elementos_exc.append(j)
    
    return eliminar_repetidos(elementos_exc)
    

def eliminar_repetidos(numeros: list) -> list:
    sin_repe = []
    
    for i in numeros:
        if i not in sin_repe:
            sin_repe.append(i)
    
    return sin_repe






def contar_traducciones_iguales(ingles: dict, aleman: dict) -> int:
    contador : int = 0
    for k in aleman:
        for j in ingles:
            if aleman[k] == ingles[j]:
                contador += 1

    return contador 
#aleman = {"Mano": "Hand", "Pie": "Fuss", "Dedo": "Finger", "Cara": "Gesicht"}
#ingles = {"Pie": "Foot", "Dedo": "Finger", "Mano": "Hand"}
#res deberia ser 2 






def cantidad_apariciones(l: list, e:int) -> int:
    contador: int = 0

    for i in l:
        if e == i:
            contador += 1
    
    return contador 


def convertir_a_diccionario(l:list) -> dict:
    resultado: dict = {}

    for i in l:
        if not i in resultado:
            resultado[i] = 1
        else: 
            resultado[i] += 1 
    
    return resultado 



 

