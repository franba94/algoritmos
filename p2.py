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
   res:bool = True
   for i in range(len(s)-1):
       if s[i] > s[i+1]:
           res = False 
   return res 


def palabras(s:[[str]]) -> bool: 
    res:bool = False
    for i in range (len(s)):
        if len(s[i]) > 7:
            res = True
    return res  


def palindromo(s:list) -> bool:
    res: bool = False 
    if s == s[::-1]:
        res = True
    return res


def tiene_un_numero(contraseña: str) -> bool:
    i: int = 0
    vale_condicion: bool = False 
    
    while i < len(contraseña) and not(contraseña[i] >= '0' and contraseña[i] <= '9'):
        i += 1 
    vale_condicion: bool = i < len(contraseña)
    return vale_condicion 


def hay_min(contraseña: str) -> bool: 
    i: int = 0
    vale_condicion: bool = False 

    while i < len(contraseña) and not(contraseña[i] >= 'a' and contraseña[i] <= 'z'):
        i += 1
    vale_condicion: bool = i < len(contraseña)
    return vale_condicion

def hay_min2(contraseña:str) -> bool:
    i: int = 0
    vale_condicion: bool = False

    while i < len(contraseña):
        if (contraseña[i] >= 'a' and contraseña[i] <= 'z'):
            vale_condicion: bool = True
        i += 1  
    return vale_condicion 

def hay_mayus(contraseña:str) -> bool:
    i: int = 0
    vale_condicion: bool = False

    while i < len(contraseña):
        if (contraseña[i] >= 'A' and contraseña[i] <= 'Z'):
            vale_condicion: bool = True 
        i += 1
    return vale_condicion

def fortaleza(contraseña: str) -> str:
    if (len(contraseña) > 8 and hay_min(contraseña) and hay_mayus(contraseña) and tiene_un_numero(contraseña)):
        return "VERDE"
    if len(contraseña) < 5:
        return "ROJA"
    else:
         return "AMARILLA" 
    
def historial_bancario(historial: list) -> int:
    saldo: int = 0
    for i in historial:
        if i[0] == "I":
            saldo += i[-1]
        elif i[0] == "R":
            saldo = saldo - i[-1]
    return saldo



def recorrer_palabra(palabra: str) -> bool:
    vocal: int = 0 
    i: int = 0
   

    while i < len(palabra):
        if palabra[i] == 'a' or 'e' or 'i' or 'o' or 'u':
            vocal += 1
            i += 1 
            if vocal >= 3:
                return True 
    return False 


def posiciones_pares_cero(numeros: list) -> int:
    
    for i in range(0,len(numeros),2):
        numeros[i] = '0'

    return numeros   

    
def cadena_sin_vocales(palabra: list) -> str: 
    vocales = "aeiou"
    palabra_nueva= ""

    for letra in palabra:
         if letra not in vocales:
            palabra_nueva = palabra_nueva + letra 
    
    return palabra_nueva 


def eliminar_repetidos(numeros: list) -> int:
    sin_repe = []
    
    for i in numeros:
        if i not in sin_repe:
            sin_repe.append(i)
    
    return sin_repe 


def lista_estudiantes() -> list:
    lista_nombres = []
    nombre: str = ""
    
    while nombre != "listo":
         nombre = input("nombre: ")
         lista_nombres.append(nombre)
         if nombre == "listo":
            lista_nombres.pop()
    return(lista_nombres)

def monedero_electronico() -> list:
    historial = []
    saldo: int = 0
    accion : str = ""
    
    while accion != "x":
          accion = input("ingrese un comando: ")
          
          if accion == "c":
             monto = int(input("ingrese un monto: "))
             saldo = saldo + monto
             historial.append ((accion, monto))
          
          elif accion == "d":
              monto = int(input("ingrese un monto: "))
              saldo = saldo - monto
              historial.append ((accion, monto))

    return f"({historial}, saldo: {saldo})" 
            
      
         



