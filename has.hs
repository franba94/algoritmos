longitud :: [Int] -> Int 
longitud [] = 0 
longitud (x:xs) = 1 + longitud xs 


ultimo :: [Int] -> Int
ultimo [x] = x 
ultimo (x:xs) = ultimo xs 

principio :: [Int] -> [Int]
principio [x] = [] 
principio (x:xs) = [x] ++ (principio xs) 

reverso :: [Int] -> [Int] 
reverso [] = []
reverso (x:xs) = ultimo (x:xs) : reverso(principio (x:xs)) 

pertenece :: Int -> [Int] -> Bool
pertenece n [] = False
pertenece n (x:xs) | n == x = True 
                   | otherwise = pertenece n xs 

todosIguales :: [Int] -> Bool
todosIguales [x] = True
todosIguales (x:y:ys) = x == y && todosIguales ys 

todosDistintos :: [Int] -> Bool
todosDistintos [] = True
todosDistintos [x] = True
todosDistintos (x:y:ys) | x /= y = todosDistintos (x:ys)
                        | otherwise = False 


hayRepetidos :: [Int] -> Bool
hayRepetidos [] = False
hayRepetidos (x:xs) | pertenece x xs = True
                    | otherwise = hayRepetidos xs 



quitar :: Int -> [Int] -> [Int]
quitar _ [] = []
quitar n (x:xs) | n == x = xs
                | otherwise = x : quitar n (x:xs) 


quitarTodos :: Int -> [Int] -> [Int]
quitarTodos _ [] = []
quitarTodos n (x:xs) | n == x = quitarTodos n xs
                     | otherwise = x : quitarTodos n xs 


eliminarRepetidos :: [Int] -> [Int]
eliminarRepetidos [] = []
eliminarRepetidos (x:xs) | hayRepetidos (x:xs) = x : (eliminarRepetidos (quitarTodos x (x:xs)))
                         | otherwise = x : (eliminarRepetidos xs)


perteneceA :: [Int] -> [Int] -> Bool
perteneceA [] _ = True
perteneceA (x:xs) (y:ys) | pertenece x (y:ys) && perteneceA xs (y:ys) = True
                         | otherwise = False

mismosElementos :: [Int] -> [Int] -> Bool 
mismosElementos (x:xs) (y:ys) = perteneceA (x:xs) (y:ys) && perteneceA (y:ys) (x:xs) 

capicua :: [Int] -> Bool
capicua [_] = True
capicua [] = True
capicua (x:xs) | x == ultimo (x:xs) && capicua (principio xs) = True
               | otherwise = False 


sumatoria :: [Int] -> Int
sumatoria [] = 0
sumatoria (x:xs) = x + sumatoria xs 

productoria :: [Int] -> Int
productoria [] = 1 
productoria (x:xs) = x * productoria xs 


maximo :: [Int] -> Int
maximo [x] = x 
maximo (x:y:xs) | x >= y = maximo (x:xs)
                | otherwise = maximo (y:xs)

sumarN :: Int -> [Int] -> [Int]
sumarN n [] = [] 
sumarN n (x:xs) = (n + x) : sumarN n xs  


sumarElPrimero :: [Int] -> [Int]
sumarElPrimero [] = []
sumarElPrimero (x:xs) = sumarN x (x:xs)


sumarElUltimo :: [Int] -> [Int]
sumarElUltimo (x:xs) = sumarN (ultimo (x:xs)) (x:xs)


pares :: [Int] -> [Int]
pares [] = []
pares (x:xs) | mod x 2 == 0 = x : pares xs
             | otherwise = pares xs 


multiplosDeN :: Int -> [Int] -> [Int]
multiplosDeN n [] = []
multiplosDeN n (x:xs) | mod x n == 0 = x : multiplosDeN n xs 
                      | otherwise = multiplosDeN n xs   

ordenar :: [Int] -> [Int]
ordenar [] = [] 
ordenar (x:xs) = (minimo (x:xs)) : ordenar(quitarTodos (minimo(x:xs)) (x:xs))

minimo :: [Int] -> Int
minimo [x] = x 
minimo (x:y:xs) | x <= y = minimo (x:xs)
                | otherwise = minimo (y:xs)


            












