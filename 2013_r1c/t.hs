
sample = unlines ["1", "1 9"]

main = interact solve

solve = unlines . formatSolution . solveCases . parseCases . drop 1 . lines

parseCases = id

solveCases = id

formatSolution = zipWith render [1..]
  where render index sol = "Case #" ++ show index ++ ": " ++ show sol






toInt :: String -> [Int]
toInt = map read . words 
