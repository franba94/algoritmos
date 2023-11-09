longitud :: [Int] -> Int 
longitud [] = 0 
longitud (x:xs) = 1 + longitud xs 

sumatoria :: [Int] -> Int
sumatoria [] = 0
sumatoria (x:xs) = x + sumatoria xs 

maximo :: [Int] -> Int
maximo [x] = x 
maximo (x:y:xs) | x >= y = maximo (x:xs)
                | otherwise = maximo (y:xs)

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
               







