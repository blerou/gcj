import Data.List

main = do
  cases <- getContents
  putStr $ unlines . solve . tail . lines $ cases

solve :: [String] -> [String]
solve cases = 
  let results = solveCase cases
  in zipWith (\i result -> "Case #" ++ show i ++ ": " ++ format result) [1..] results

solveCase :: [String] -> [Double]
solveCase [] = []
solveCase (_:line:xs) = (goroSort . parse $ line) : solveCase xs

parse :: String -> [Int]
parse = map read . words

goroSort :: [Int] -> Double
goroSort nums = 
  let sorted = sort nums
      numOfDiff = sum [1 | i <- [0..length nums - 1], nums !! i /= sorted !! i]
  in fromIntegral numOfDiff

format :: Double -> String
format = show