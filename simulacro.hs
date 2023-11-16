relacionesValidas :: [(String,String)] -> Bool 
relacionesValidas [] = True
relacionesValidas ((a,b):xs) | a == b = False 
                             | pertenece (a,b) xs || pertenece (b,a) xs = False
                             | otherwise = relacionesValidas xs

pertenece ::  Eq t => (t,t) -> [(t,t)] -> Bool
pertenece (a,b) [] = False
pertenece (a,b) ((c,d):xs) | (a,b) == (c,d) = True
                           | otherwise = pertenece (a,b) xs 




--personas :: [(String,String)] -> [String]
--personas [] = []
--personas ((a,b):xs) = eliminarRepetidos(a : b : personas xs)

pertenece2 :: (Eq t) => t -> [t] -> Bool
pertenece2 a [] = False
pertenece2 a (x:xs) | a == x = True 
                   | otherwise = pertenece2 a xs 

eliminarRepetidos :: (Eq t) => [t] -> [t] 
eliminarRepetidos [] = []
eliminarRepetidos (x:xs) | 


