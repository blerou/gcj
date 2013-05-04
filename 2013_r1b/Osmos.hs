
import Data.List

sample = unlines ["4", "2 2", "2 1", "2 4", "2 1 1 6"]

main = interact solve

solve = unlines . formatSolution . solveCases . parseCases . drop 1 . lines


parseCases = parseCases'
parseCases' []    = []
parseCases' (armin:more:lines) = (a, motes) : parseCases' lines
           where [a, _] = toInt armin
                 motes = toInt more

solveCases = solveCases'
solveCases' [] = []
solveCases' ((a, motes):rem) = solveMote a motes 0 : solveCases' rem

formatSolution = zipWith render [1..]
  where render index sol = "Case #" ++ show index ++ ": " ++ show sol


solveMote a motes ops
          | null larger  = ops
          | null smaller && sameSize = ops + length larger
          | null smaller = min (ops + length larger) (solveMote nextSize larger (ops + 1))
          | otherwise    = solveMote (a + sum smaller) larger ops
          where (smaller, larger) = partition (\x -> x < a) motes
                nextSize = 2*a - 1
                sameSize = a == nextSize


toInt :: String -> [Int]
toInt = map read . words 