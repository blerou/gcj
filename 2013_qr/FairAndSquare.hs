import Data.List (sort)

data Interval = Full Int | Partial Int Int deriving (Show)

sample = unlines ["3", "1 4", "10 120", "100 1000"]

main = interact solve

solve = unlines . showCases . solveCases . parseCases . drop 1 . lines

parseCases = map (map read . words)

solveCases = map (\[a, b] -> solveCase a b)

showCases = zipWith renderer [1..] 
  where renderer i c = "Case #" ++ show i ++ ": " ++ show c



solveCase a b = numOfPalindroms a' b'
  where a' = ceiling $ sqrt a
        b' = floor $ sqrt b


numOfPalindroms a b
  | a > b     = 0
  | otherwise = numOfPalindroms' nextInterval (upperBound+1, b)
  where nextInterval = 
          if a == l && upperBound == a'
          then Full (length $ show a)
          else Partial a upperBound
        upperBound = min a' b
        a' = 10 ^ (length $ show a) - 1
        l  = 10 ^ ((length $ show a) - 1)

numOfPalindroms' (Full n)        (a', b') = 9 * 10 ^ ((n-1) `div` 2) + numOfPalindroms a' b'
numOfPalindroms' (Partial li hi) (a', b') = calcPals li hi + numOfPalindroms a' b'

calcPals x y
  | x > y     = calculateOn y x
  | otherwise = calculateOn x y 
  where calculateOn low high = sum [1 | i <- [low..high], show i == (reverse $ show i)]
{-
calcPals []   _    = 1
calcPals numX numY = (toInt b - toInt a) * calcPals (remNum numX) (remNum numY)
  where [_, a, b, _] = sort [head numX, head numY, last numX, last numY]
        toInt ch = read (ch:[])
        remNum s = take (length s - 2) (drop 1 s)
-}      