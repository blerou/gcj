import Data.List

type Pair = (Int, Int)

main = do
  cases <- getContents
--  putStrLn $ show $ filter (\i -> length i > 1) $ group result
--  where result = sort $ recycledNumbers [1111, 2222]
  putStr $ unlines . solve . tail . lines $ cases

solve :: [String] -> [String]
solve lines = 
  let results = map (length . nub . recycledNumbers . parse) lines
  in zipWith (\i r -> "Case #" ++ show i ++ ": " ++ format r) [1..] results

parse :: String -> [Int]
parse = map read . words

recycledNumbers :: [Int] -> [Pair]
recycledNumbers [a, b] = foldl (countANumber b) [] [start..b]
  where start = if a < 10 then 10 else a

countANumber :: Int -> [Pair] -> Int -> [Pair]
countANumber top acc n = foldl (countRotations top n) acc rotations
  where len = length $ show n
        rotations = zipWith (\i n -> 10^(len-i) * (rem n (10^i)) + div n (10^i)) [1..len] $ repeat n

countRotations :: Int -> Int -> [Pair] -> Int -> [Pair]
countRotations top base acc n = if n > base && n <= top then (base,n):acc else acc


format :: Int -> String
format = show