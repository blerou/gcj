
sample = unlines ["1", "1 9"]

main = interact solve

solve = unlines . formatSolution . solveCases . parseCases . drop 1 . lines

parseCases cases = map parseCase cases

solveCases cases = map solveCase cases

formatSolution = zipWith render [1..]
  where render index ringCount = "Case #" ++ show index ++ ": " ++ show ringCount


parseCase :: String -> (Int, Int)
parseCase line = (r, t)
  where [r, t] = toInt line
        toInt = map read . words

solveCase :: (Int, Int) -> Int
solveCase (r, t) = floor ((t - 2*(r :: Double) + 3) / 2)  -- (2*t - 2*a1 + d) / d  -- a1 = 2*r + 1
