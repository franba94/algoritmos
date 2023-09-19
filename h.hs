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