fibonacci :: Int -> Int
fibonacci 0 = 0
fibonacci 1 = 1
fibonacci n = fibonacci (n-1) + fibonacci (n-2)


parteEntera :: Float -> Int
parteEntera n | n < 1 = 0
              | otherwise = 1 + parteEntera (n - 1)

esDivisible :: Int -> Int -> Bool
esDivisible x y | x - y == 0 = True
                | x - y /= 0 = False 
                | otherwise = esDivisible (x-y) y 
