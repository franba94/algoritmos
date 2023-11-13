-- Ejercicio 1
votosEnBlanco :: [(String, String)] -> [Int] -> Int  -> Int
votosEnBlanco _ (x:xs) n | sumatoria (x:xs) == n = 0
                               | otherwise = n - (sumatoria (x:xs))

sumatoria :: [Int] -> Int
sumatoria [] = 0
sumatoria (x:xs) = x + sumatoria xs 


-- Ejercicio 2
formulasValidas :: [(String, String)] -> Bool
formulasValidas [] = True 
formulasValidas ((a,b):xs) | a == b = False 
                           | pertenece (a,b) xs || pertenece (b,a) xs = False 
                           | otherwise = formulasValidas xs 

pertenece ::  Eq t => (t,t) -> [(t,t)] -> Bool
pertenece (a,b) [] = False
pertenece (a,b) ((c,d):xs) | a == c || b == d || a == d || b == c = True
                           | otherwise = pertenece (a,b) xs 

                     

