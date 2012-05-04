import Data.List

main = do
  cases <- getContents
  putStr $ unlines . solve . tail . lines $ cases

solve :: [String] -> [String]
solve lines = 
  let results = map (length . recycledNumbers . parse) lines
  in zipWith (\i r -> "Case #" ++ show i ++ ": " ++ format r) [1..] results

parse :: String -> [String]
parse = words

recycledNumbers :: [String] -> [String]
recycledNumbers [a, b] = foldl (countANumber b) [] [(read a::Int)..(read b::Int)]

countANumber :: String -> [String] -> Int -> [String]
countANumber top acc base = foldl (countRotations top num) acc rotations
  where num = show base
        rotations = nub . init . tail $ zipWith (++) (tails num) (inits num)

countRotations :: String -> String -> [String] -> String -> [String]
countRotations top base acc n = if n > base && n <= top then n:acc else acc

format :: Int -> String
format = show