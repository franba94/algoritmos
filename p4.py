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
    
print(jugarCartonDeBingo(carton, q))

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

print(agruparPorLongitud('ejercicio_19.txt'))












    