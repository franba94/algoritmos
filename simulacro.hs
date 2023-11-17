relacionesValidas :: [(String,String)] -> Bool 
relacionesValidas [] = True
relacionesValidas ((a,b):xs) | a == b = False 
                             | pertenece (a,b) xs || pertenece (b,a) xs = False
                             | otherwise = relacionesValidas xs

pertenece ::  Eq t => (t,t) -> [(t,t)] -> Bool
pertenece (a,b) [] = False
pertenece (a,b) ((c,d):xs) | (a,b) == (c,d) = True
                           | otherwise = pertenece (a,b) xs 




personas :: [(String,String)] -> [String]
personas [] = []
personas ((a,b):xs) = eliminarRepetidos(a : b : personas xs)

pertenece2 :: (Eq t) => t -> [t] -> Bool
pertenece2 a [] = False
pertenece2 a (x:xs) | a == x = True 
                   | otherwise = pertenece2 a xs 

eliminarRepetidos :: (Eq t) => [t] -> [t] 
eliminarRepetidos [] = []
eliminarRepetidos (x:xs) | pertenece2 x xs = eliminarRepetidos xs 
                         | otherwise = x : eliminarRepetidos xs  



amigosDe :: String -> [(String, String)] -> [String]
amigosDe x [] = []
amigosDe x ((a,b):xs) | x == a = b : amigosDe x xs 
                      | x == b = a : amigosDe x xs
                      | otherwise = amigosDe x xs


--personaConMasAmigos :: [(String, String)] -> String
 

cantidadAmigos :: String -> [(String, String)] -> Int
cantidadAmigos x [] = 0
cantidadAmigos x ((a,b):xs) | x /= a && x /= b = 0
                            | otherwise = 1 + cantidadAmigos x xs 


        

