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

