import math 


def imprimir_hola_mundo():
    print ("hola mundo")
    
    
def imprimir_un_verso():
    print ("lasksajjksdajklsdajklsadjkldas\nasdasdasdasdasdsad\nasdasds\n")
    
    
def raizDe2() -> float:
    print (round(math.sqrt(2), 2)) 
    

def factorial_de_dos() -> int:
    print (2*1)
    
    
def perimetro() -> float:
    return 2*math.pi
    
    
def imprimir_saludo(nombre: str):
   print("Hola " + nombre)
   
   
def raiz_cuadrada_de(x: int) -> float:
   return math.sqrt(x)


def fahrenheit_a_celsius(t: int) -> int:
    return round(((t-32)*5) / 9)


def imprimir_dos_veces(x: str):
    x: str = "lasksajjksdajklsdajklsadjkldas\nasdasdasdasdasdsad\nasdasds\n"
    print ( x + x )
    

    
def es_multiplo_de(x: int, y: int) -> bool:
    return x % y == 0


def es_par(x: int) -> bool:
    return (es_multiplo_de(x, 2)) 
    
    
def es_nombre_largo(e: str) -> bool:
    return len(e) >= 3 and len(e) <= 8 
    
def cantidad_de_pizzas(comensales: int, porci_min: int) -> int:
    if comensales * porci_min <= 8: 
       return 1
    else:
     return round ((comensales * porci_min) / 8 + 1) 
    

def alguno_es_0(x: int, y: int) -> bool:
    return x == 0 or y == 0 


def ambos_son_0(x: int, y: int) -> bool:
    return x == 0 and y == 0 


def es_bisiesto(x: int) -> bool:
    return es_multiplo_de(x, 400) or ((es_multiplo_de(x, 4)) and not (es_multiplo_de(x, 100)))


def peso_pino(x: int) -> int:
    if x <= 3:
       return x*300
    else:
        return (x-3)*200 + 3*300
    
def es_peso_util(x: int) -> bool: 
    return x >= 400 and x<= 1000


def sirve_pino2(x: int) -> bool:
    return es_peso_util(peso_pino(x))


def devolver_el_doble_si_es_par(x: int) -> int:
    res: int = 0
    if x % 2 == 0:
      res = x*2
    else:
         res = x
    return res

def devolver_valor_si_es_par_sino_el_que_sigue(x: int) -> int:
    if x % 2 == 0:
        return x
    else:
        return x + 1 
    
def devolver_blabla(x: int) -> int:
    if es_multiplo_de(x,3):
        return x*2
    elif es_multiplo_de(x,9):
        return x*3
    else:
        return x          

def lindo_nombre(nombre: str): 
    if len(nombre) >= 5: 
       return "tu nombre tiene muchas letras!"
    else:
        return "tu nombre tiene menos de 5 caracteres"
    

def elRango(n: int):
    if n < 5:
        return "menor a 5"
    elif n >= 10 and n <= 20:
        return "entre 10 y 20"
    else:
        return "mayor a 20"
    

def agarraLaPala(x: str, n: int) -> str:
    if x == "f" and (n > 17 and n < 60):
        return "agarra la pala"
    elif x == "m" and (n > 17 and n < 65):
        return "agarra la pala"
    else:
         return "tomate el palo"
    
def hasta_10():
    n: int = 1 
    while n <= 10:
        print (n)
        n = n + 1


def imprime_pares_10_40():
   n: int = 10
   while n <= 40:
         print (n)
         n = n + 2 
         

def eco():
    n: int = 1
    while n <= 10:
        print("eco")
        n = n + 1


def despegue(n: int):
   while n > 0:
         print (n)
         n = n - 1 
   print("Despegue")


def viaje_tiempo(partida: int, llegada: int) -> str:
    while partida > llegada:
          print ("viajo un año al pasado, estamos en el año: ", partida -1 )
          partida = partida - 1 


def viaje_tiempo2(partida: int) -> str:
    while partida > 384:
          print ("viajo veinte años al pasado, estamos en el año: ", partida - 20 )
          partida = partida - 20


def hasta10_dos():
    for i in range (10, 0, -1):
        print (i)


def imprime_pares_10_40_for():
   for n in range(10, 42, 2):
       print (n)
       

def eco2():
    n: int = 1 
    for n in range (1, 11, 1):
        print ("eco")


def despegue_for(n: int):
   for i in range (0, n, 1):
       print(n-i)
   print("Despegue") 


def viaje_tiempo_for(partida: int, llegada: int) -> str:
    for i in range (partida, llegada, -1):
        print("viajo un año al pasado, estamos en el año: ", i)


def viaje_tiempo2_for(partida: int) -> str:
    for i in range (partida, 384, -1):
        print("viajo 20 años al pasado, estamos en el año: ", i)










   
   
   
    
         
         
      
