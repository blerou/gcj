import Data.List

main = do
  cases <- getContents
  putStr $ unlines . solve . tail . lines $ cases

solve :: [String] -> [String]
solve cases = zipWith (\i r -> "Case #" ++ show i ++ ": " ++ format r) [1..] results
  where results = solveCase cases

solveCase :: [String] -> [String]
solveCase [] = []
solveCase (n:cases) = diamond inher : solveCase (drop classCount cases)
  where classCount = read n :: Int
        inher = zip [1..] . map parse . take classCount $ cases

parse :: String -> [Int]
parse = tail . map read . words

diamond :: [(Int, [Int])] -> String
diamond inherits = if any (\g -> length g > 1) . group . concat . map (resolve inherits) $ inherits then "Yes" else "No"

resolve :: [(Int, [Int])] -> (Int, [Int]) -> [(Int, Int)]
resolve _ (c, []) = [(0, c)]
resolve inherits (c, ds) = map (\(i,j) -> (c,j)) . concat . map (resolve inherits) . filter (\(j,_) -> j `elem` ds) $ inherits

format = show
