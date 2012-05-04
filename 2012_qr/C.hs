import Data.List

main = do
  cases <- getContents
  putStr $ unlines . solve . tail . lines $ cases

solve :: [String] -> [String]
solve lines = 
  let results = map (recycledNumbers . parse) lines
  in zipWith (\i r -> "Case #" ++ show i ++ ": " ++ format r) [1..] results

parse :: String -> [String]
parse = words

recycledNumbers :: [String] -> Int
recycledNumbers [a, b] = foldl (countANumber b) 0 [(read a::Int)..(read b::Int)]

countANumber :: String -> Int -> Int -> Int
countANumber top sum base = sum + recycleds
  where num = show base
        rotations = nub . init . tail $ zipWith (++) (tails num) (inits num)
        recycleds = length $ filter (\n -> n > num && n <= top) rotations

format :: Int -> String
format = show