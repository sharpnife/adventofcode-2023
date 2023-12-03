import Data.Char as C

getDigit (x:xs) = if C.isDigit x then C.digitToInt x else getDigit xs

f x = (getDigit x) * 10 + (getDigit $ reverse x)

getDigit2 [] = []
getDigit2 (x:xs)
      | C.isDigit x              = [C.digitToInt x] ++ getDigit2 xs
      | take 3 (x:xs) == "one"   = [1] ++ getDigit2 xs
      | take 3 (x:xs) == "two"   = [2] ++ getDigit2 xs
      | take 5 (x:xs) == "three" = [3] ++ getDigit2 xs
      | take 4 (x:xs) == "four"  = [4] ++ getDigit2 xs
      | take 4 (x:xs) == "five"  = [5] ++ getDigit2 xs
      | take 3 (x:xs) == "six"   = [6] ++ getDigit2 xs
      | take 5 (x:xs) == "seven" = [7] ++ getDigit2 xs
      | take 5 (x:xs) == "eight" = [8] ++ getDigit2 xs
      | take 4 (x:xs) == "nine"  = [9] ++ getDigit2 xs
      | otherwise = getDigit2 xs 

f2 x = (head $ getDigit2 x) * 10 + (head $ reverse $ getDigit2 x)

main = do
       s <- readFile "inp.txt"
       print $ "Part 1: " ++ show (sum $ map f $ lines s)
       print $ "Part 2: " ++ show (sum $ map f2 $ lines s)
