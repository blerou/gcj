main = do
  cases <- getContents
  putStr $ unlines . solve . drop 1 . lines $ cases

solve :: [String] -> [String]
solve cases =
  let results = map (dancingGooglers . parse) cases
  in zipWith (\i r -> "Case #" ++ show i ++ ": " ++ format r) [1..] results

parse :: String -> [Int]
parse = map read . drop 1 . words

dancingGooglers :: [Int] -> Int
dancingGooglers (s:p:ts) = sureCount + (if surprisingCount > s then s else surprisingCount)
  where
    tPairs = map (\t -> (div t 3, rem t 3)) ts
    sureCount = length $ filter sureFunc tPairs
    sureFunc (d, r)
      | d >= p              = True
      | d + 1 == p && r > 0 = True
      | otherwise           = False
    surprisingCount = length $ filter surprisingFunc tPairs
    surprisingFunc (d, r)
      | d > 0 && d + 1 == p && r == 0 = True
      | d + 2 == p && r == 2          = True
      | otherwise                     = False

format :: Int -> String
format = show