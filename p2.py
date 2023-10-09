def pertenece(s:list, e:int) -> bool:
    res: bool = False
    
    for i in range(0,len(s),1):
        if (s[i] == e):
            res = True
    return res 

def divideATodos (s:list,e:int) -> bool:
    for i in s:
        if i % e != 0:
            return False
    return True
      

def suma_total(s: list) -> int:
    res: int = 0
    i: int = 0
    while (i < len(s)):
    	res += s[i]
    	i += 1 
    return res


def ordenados(s:list) -> bool:
   res : bool = True
   for i in range(len(s)-1):
       if s[i] > s[i+1]:
           res = False 
   return res 



    


def tiene_un_numero(contraseña: str) -> bool:
    i: int = 0
    vale_condicion: bool = False 
    
    while i < len(contraseña) and not(contraseña[i] >= '0' and contraseña[i] <= '9'):
        i += 1 
    vale_condicion: bool = i < len(contraseña)
    return vale_condicion 


def es_par(num: int) -> bool:
    return(num % 2 == 0)


def reemplazar_pares(s:list) -> None:
    indice_actual: int = 0
    longitud: int = len(s)
    while (indice_actual < longitud):
        if (es_par(indice_actual)):
            s[indice_actual] = 0
        indice_actual += 1

def pertenece_a_cada_uno(s:[[int]], e:int) -> [bool]:
    res_pertenece:[] = []
    
    indice_actual: int = 0
    longitud: int = len(s)
    
    while (indice_actual < longitud):
      lista_actual:[int] = s[indice_actual]
      res_pertenece.append(pertenece(lista_actual,e))
      indice_actual += 1

    return res_pertenece
        





