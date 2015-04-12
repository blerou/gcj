
sample = unlines ["1", "quartz 3", "straight 3", "gcj 2", "tsetse 2"]

main = interact solve

solve = unlines . formatSolution . solveCases . parseCases . drop 1 . lines

parseCases = map parseCase
parseCase :: String -> (String, Int)
parseCase l = (s, read n)
          where [s, n] = words l

solveCases = map solveCase
solveCase (s, n) = sum $ take (calcC s n) $ reverse [0..l - n + 1]
          where l = length s

calcC s n = sum $ map (\x -> x-n+1) $ filter (>=n) $ calcC' s
calcC' [] = []
calcC' (l:ls) 
       | isVowel l = calcC' (dropWhile isVowel ls)
       | otherwise = 1 + (length $ takeWhile (not.isVowel) ls) : calcC' (dropWhile (not.isVowel) ls)
       where isVowel l = l `elem` "aeiou" 

formatSolution = zipWith render [1..]
  where render index sol = "Case #" ++ show index ++ ": " ++ show sol






toInt :: String -> [Int]
toInt = map read . words 
