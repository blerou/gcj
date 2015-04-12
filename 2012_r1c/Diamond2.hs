import Data.List

main = do
  cases <- getContents
  putStr $ unlines . solve . tail . lines $ cases

solve :: [String] -> [String]
solve cases = zipWith (\i r -> "Case #" ++ show i ++ ": " ++ format r) [1..] results
  where results = solveCase cases

solveCase :: [String] -> [String]
solveCase [] = []
solveCase (n:cases) = diamond inheritMap : solveCase (drop classCount cases)
  where classCount = read n :: Int
        successors = map parse . take classCount $ cases
        inheritMap = concat $ zipWith (\i s -> [(i, c) | c <- s]) [1..] successors

parse :: String -> [Int]
parse = tail . map read . words

diamond :: [(Int, Int)] -> String
diamond inherits = show $ resolve inherits multiPairs
  where multi = map head . filter (\g -> length g > 1) . group . map fst $ inherits
        multiPairs = filter (\(c,_) -> c `elem` multi) inherits

resolve :: [(Int, Int)] -> [(Int, Int)] -> [(Int, Int)]
resolve inherits multiList = multiList

format = show
