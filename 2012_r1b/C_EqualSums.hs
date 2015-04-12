main = do
  cases <- getContents
  putStr $ unlines . solve . drop 1 . lines $ cases

solve cases = zipWith (\i r -> "Case #" ++ show i ++ ": " ++ format r) [1..] results
  where results = map (equalSums . parse) cases
        
parse :: String -> [Int]
parse = tail . map read . words

equalSums nums = 

format = show