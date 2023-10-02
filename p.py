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
    

def devolver_el_doble_si_es_par(x: int) -> int:
    res: int = 0
    if x % 2 == 0:
      res = x*2
    else:
         res = x
    return res  

      
def imprime_pares_10_40():
   n: int = 10
   while n <= 40:
         print (n)
         n = n + 2 
         
def imprime_pares_10_40_for():
   for n in range(10, 42, 2):
       print (n)
       
def despegue(n: int):
   while n > 0:
         print (n)
         n = n - 1 
   print("Despegue")
   

def despegue_for(n: int):
   for i in range (0, n, 1):
       print(n-i)
   print("Despegue") 
   
   
   
    
         
         
      
