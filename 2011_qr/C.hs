import Data.Bits

main = do
  cases <- getContents
  putStr $ unlines . solve . (drop 1) . lines $ cases

solve :: [String] -> [String]
solve lines = 
  let results = solveCase lines
  in zipWith (\i result -> "Case #" ++ show i ++ ": " ++ format result) [1..] results

solveCase :: [String] -> [Either String Int]
solveCase [] = []
solveCase (_:line:xs) = (candySplitting . parse $ line) : solveCase xs

parse :: String -> [Int]
parse = map read . words

candySplitting :: [Int] -> Either String Int
candySplitting numbers 
  | foldl xor 0 numbers == 0 = Right (sum numbers - minimum numbers)
  | otherwise                = Left "NO"

format :: Either String Int -> String
format (Left x) = x
format (Right y) = show y