#ARCHIVOS
def contar_lineas(nombre_archivo_input: str) -> int:
    lineas: int = 0
    archivo_input = open(nombre_archivo_input, "r")
    nombre_archivo_input: str = 'himno.txt'
    for line in archivo_input.readlines():
        lineas = lineas + 1 
    return lineas 
    
    archivo_input.close() 



def pertenece(palabras: list, q:str ) -> bool:
    palabras = palabras.split()
    for p in palabras:
        if p == q:
            return True
    return False 

def existe_palabra(palabra: str, nombre_archivo_input: str) -> bool:
    archivo_input = open(nombre_archivo_input, "r")
    nombre_archivo_input: str = 'himno.txt'
    for line in archivo_input.readlines():
        if  pertenece(line, palabra):
            return True
   
    return False
   
    archivo_input.close()


def cantidad_apariciones(nombre_archivo_input: str, palabra: str) -> int:
    archivo_input = open(nombre_archivo_input, "r")
    nombre_archivo_input: str = 'himno.txt'
    cantidad = 0
    texto_nuevo = []
    
    for line in archivo_input.readlines():
        texto_formateado = line.split()
        
        for word in texto_formateado:
            word = word.lower()
            word = word.replace('¡','').replace('!','').replace('.','')
            word = word.replace(';','').replace(',','').replace(':','')
            texto_nuevo.append(word)


    for p in texto_nuevo:
        if palabra == p:
            cantidad += 1 

    return cantidad
    
    archivo_input.close() 

            


def clonarSinComentarios(nombre_archivo_input: str) -> None:
    
    #abro archivo de input
    archivo_input = open(nombre_archivo_input, "r")

    #idem output
    nombre_archivo_output: str = 'ejercicio_2_output.txt'
    archivo_output = open(nombre_archivo_output, "w")

    for line in archivo_input.readlines():
        if not es_un_comentario(line):
            archivo_output.write(line)

    archivo_input.close()
    archivo_output.close()

def es_un_comentario(line: str) -> bool:
    for c in line:
        if c != '':
            if c == '#':
                return True # es un comentario
            return False # NO es un comentario
    return False #caso todos chars ''



#def reverso(nombre_archivo_input: str) -> None:
   # archivo_input = open(nombre_archivo_input, "r")
   # nombre_archivo_output: str = 'himno_reverso.txt'
   # archivo_output = open(nombre_archivo_output, "w")
    

   # for line in archivo_input.readlines():
      #  for word in range(len(archivo_input)-1,-1,-1):
            

   # archivo_output.close()

def agregar_final(nombre_archivo_input: str, frase: str) -> None:
    archivo_input = open(nombre_archivo_input, "r")
    frase_nueva = []
    for line in archivo_input.readlines():
         frase_nueva.append(line)
    
    frase_nueva.append(frase)
    archivo_input = open(nombre_archivo_input, "w")

    for line in frase_nueva:
        archivo_input.write(line) 
    #mete la palabra despues de donde quede el puntero(si
    # queda al final da un salto de linea)
    archivo_input.close()


def agregar_principio(nombre_archivo_input: str, frase: str) -> None:
    archivo_input = open(nombre_archivo_input, "r")
    frase_nueva = []
    for line in archivo_input.readlines():
         frase_nueva.append(line)
    
    frase_nueva.insert(0,f"{frase}\n")

    archivo_input:str = open(nombre_archivo_input,"w")
    for line in frase_nueva:
        archivo_input.write(line)

    archivo_input.close()


#PILAS
import random
from queue import LifoQueue

def generar_numeros_azar(n: int, desde: int, hasta: int) -> LifoQueue:
    pila: LifoQueue = LifoQueue()

    for i in range(n):
        pila.put(random.randint(desde,hasta))
    
    
    #print(list(pila.queue))

    return pila


def copiar(p: LifoQueue) -> LifoQueue:
    elements: [int] = []
    while not p.empty():
        elements.append(p.get())
    p_copy: LifoQueue = LifoQueue()
    for i in range(len(elements)-1, 0-1, -1):
        p.put(elements[i])
        p_copy.put(elements[i])
    return p_copy 

def cantidad_elementos(p: LifoQueue) -> LifoQueue:
    p_copy: LifoQueue = copiar(p)
    value = 0
    while not p_copy.empty():
        p_copy.get()
        value += 1 
    return value 
    

        
p: LifoQueue = LifoQueue ()
p.put(1)
p.put(2)
p.put(3)
p.put(4)
#print(list(p.queue))
#print(cantidad_elementos(p))
        

  
from queue import LifoQueue 

def copiar(p: LifoQueue) -> LifoQueue:
    elements: [int] = []
    while not p.empty():
        elements.append(p.get())
    p_copy: LifoQueue = LifoQueue()
    for i in range(len(elements)-1, 0-1, -1):
        p.put(elements[i])
        p_copy.put(elements[i])
    return p_copy 

def buscarElMaximo(p: LifoQueue) -> int:
    p_copy: LifoQueue = copiar(p)
    value = p.get()
    while not p_copy.empty():
        next_value = p_copy.get()
        value = max(next_value, value)
    return value 

pila: LifoQueue = LifoQueue ()
pila.put(-1)
pila.put(-3)
pila.put(-4)
pila.put(-5)
#print(list(pila.queue))
#print(buscarElMaximo(pila))


#COLAS
import random
from queue import Queue

def generar_numeros_azar2(n: int, desde: int, hasta: int) -> Queue:
    cola: Queue = Queue()

    for i in range(n):
        cola.put(random.randint(desde,hasta))
    #print(list(cola.queue))
    
    return cola 


def copiarcola(cola: Queue) -> Queue:
    elements: [int] = []
    while not cola.empty():
        elements.append(cola.get())
    cola_copy: Queue = Queue()
    for i in range(len(elements)):
        cola.put(elements[i])
        cola_copy.put(elements[i])
        #print(cola.queue)
        
    return cola_copy 

c = Queue()
c.put(1)
c.put(2)
c.put(3)
print(copiarcola(c))

def cantidad_elementos2(cola: Queue) -> Queue:
    cola_copy: LifoQueue = copiar(cola)
    value = 0
    while not cola_copy.empty():
        cola_copy.get()
        value += 1 
    return value 
    
cola: Queue = Queue ()
cola.put(1)
cola.put(2)
cola.put(3)
cola.put(4)
#print(list(cola.queue))
#print(cantidad_elementos2(cola))




from queue import Queue 
import random 

def armarSecuenciaDeBingo() -> Queue:
    l: [int] = []
    for i in range(0, 99+1, 1):
        l.append(i)
    random.shuffle(l)
    result: Queue[int] = Queue()
    for elem in l:
        result.put(elem)
    return result 

q = armarSecuenciaDeBingo()
#print(q.get())

carton = [1,3,4,5,62,99,41,12,7,10,77,55]
def jugarCartonDeBingo(carton: list, bolillero: Queue) -> int:
    jugadas: int = 0
    casillas_completadas_en_carton: int = 0
    while not bolillero.empty():
        #saco una bola
        bola = bolillero.get()
        jugadas += 1 
        if bola in carton:
            casillas_completadas_en_carton += 1 
        #chequeo si gane
        if casillas_completadas_en_carton == len(carton):
            return jugadas
    
#print(jugarCartonDeBingo(carton, q))

pacientes = Queue()
pacientes.put((1,'n','cirujia'))
pacientes.put((6,'a','otorrino'))
pacientes.put((4,'x','dermatologa'))
pacientes.put((3,'y','oftalmologo'))

def pacientes_urgentes(pacientes: Queue) -> int:
    lista_pacientes: list = []
    contador = 0

    while not pacientes.empty():
        lista_pacientes.append(pacientes.get()) 
    
    for i in range(len(lista_pacientes)):
        if lista_pacientes[i][0] <= 3:
            contador += 1
    
    for i in range(len(lista_pacientes)): #aca reconstruyo la cola
        pacientes.put(lista_pacientes[i])#aca reconstruyo la cola

    #print(list(pacientes.queue))
    return contador

#print(pacientes_urgentes(pacientes))

clientes_cola = Queue()
clientes_cola.put(('n',1,True,False))
clientes_cola.put(('a',4,False,False))
clientes_cola.put(('x',2,True,True))

def a_clientes(clientes_cola: Queue) -> Queue:
    cola_de_atencion = Queue()
    lista_clientes: list = []

    while not clientes_cola.empty():
        lista_clientes.append(clientes_cola.get())
    print(lista_clientes)
    for i in range(len(lista_clientes)):
        if lista_clientes[i][3] == True:
            cola_de_atencion.put(lista_clientes[i])
            



































def agruparPorLongitud(nombre_archivo_input: str) -> dict:

    #abro archivo de input
    archivo_input = open(nombre_archivo_input, "r")

    result: dict = {}
    for line in archivo_input.readlines():
        for word in line.split():
            if len(word) not in result:
                result[len(word)] = 1 
            else:
                result[len(word)] += 1

    archivo_input.close()
    return result 

#print(agruparPorLongitud('ejercicio_19.txt'))














    
