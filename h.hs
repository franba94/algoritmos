longitud :: [Integer] -> Integer
longitud l | l == [] = 0
           | otherwise = 1 + longitud (tail l)

ultimo :: [Integer] -> Integer
ultimo [] = 0
ultimo l | longitud l == 1 = head l 
         | otherwise = ultimo (tail l)

principio :: [Integer] -> [Integer]
principio [_] = [] 
principio l | longitud l == 1 = principio l
            | otherwise = head l : [] ++ (principio (tail l))

reverso :: [t] -> [t]
reverso [x] = [x]
reverso l = reverso (tail l)  ++ [head l] 


pertenece :: Integer -> [Integer] -> Bool 
pertenece e [] = False 
pertenece e (x:xs) | e == x = True
                   | otherwise = pertenece e xs  

todosIguales :: [Integer] -> Bool
todosIguales [_] = True
todosIguales (x:y:xs) | x == y = todosIguales (x:xs) 
                      | otherwise = False

todosDistintos :: [Integer] -> Bool 
todosDistintos [_] = True
todosDistintos (x:xs) | pertenece x xs = False
                      | otherwise = todosDistintos xs 

hayRepetidos :: [Integer] -> Bool
hayRepetidos [_] = False
hayRepetidos (x:xs) | pertenece x xs = True
                    | otherwise = hayRepetidos xs

quitar :: Integer -> [Integer] -> [Integer]
quitar e [] = []
quitar e (x:xs) | e == x = xs
                | otherwise = x : quitar e xs 

quitarTodos :: Integer -> [Integer] -> [Integer]
quitarTodos e [] = [] 
quitarTodos e (x:xs) | e == x = quitarTodos e xs
                     | otherwise = x : quitarTodos e xs

eliminarRepetidos :: [Integer] -> [Integer]
eliminarRepetidos [] = [] 
eliminarRepetidos (x:xs) | hayRepetidos (x:xs) = x : eliminarRepetidos (quitarTodos x xs)  
                         | otherwise = x : eliminarRepetidos xs 

mismosElementos2 :: [Integer] -> [Integer] -> Bool
mismosElementos2 [] _ = True
mismosElementos2 (x:xs) (y:ys) | pertenece x (y:ys) = mismosElementos2 xs (y:ys)
                               | otherwise = False  


mismosElementos :: [Integer] -> [Integer] -> Bool
mismosElementos (x:xs) (y:ys) = mismosElementos2 (x:xs) (y:ys) && mismosElementos2 (y:ys) (x:xs)

capicua :: (Eq t) => [t] -> Bool
capicua (x:xs) = (x:xs) == reverso (x:xs) 

sumatoria :: [Integer] -> Integer
sumatoria [] = 0
sumatoria (x:xs) = x + sumatoria xs  

productoria :: [Integer] -> Integer
productoria [] = 1 
productoria (x:xs) = x * productoria xs 

maximo :: [Integer] -> Integer
maximo [x] = x
maximo (x:xs) | x >= maximo xs = x
              | otherwise = maximo xs 

sumarN :: Integer -> [Integer] -> [Integer]
sumarN n [x] = [n + x] 
sumarN n (x:xs) = (n + x) : sumarN n xs 

sumarElPrimero :: [Integer] -> [Integer]
sumarElPrimero [] = []
sumarElPrimero (x:xs) = sumarN x (x:xs)

sumarElUltimo :: [Integer] -> [Integer]
sumarElUltimo [] = []
sumarElUltimo (x:xs) = sumarN (ultimo (x:xs)) (x:xs)

pares :: [Integer] -> [Integer]
pares [] = []
pares (x:xs) | mod x 2 == 0 = x : pares xs 
             | otherwise = pares xs 

multiplosDeN :: Integer -> [Integer] -> [Integer]
multiplosDeN n [] = []
multiplosDeN n (x:xs) | mod x n == 0 = x : multiplosDeN n xs 
                      | otherwise = multiplosDeN n xs

ordenar :: [Integer] -> [Integer]
ordenar [] = [] 
ordenar (x:xs) = maximo (x:xs) : ordenar (quitarTodos (maximo (x:xs)) (x:xs))











