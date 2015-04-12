
main = do
     dict <- readFile "garbled_email_dictionary.txt"
     input <- getContents
     putStr $ solve dict input

solve dict input = unlines . formatSolution . solveCases (words dict) . parseCases . drop 1 . lines $ input

parseCases = id

solveCases dict cases = map (matchDict dict) cases

formatSolution = zipWith render [1..]
  where render index sol = "Case #" ++ show index ++ ": " ++ show sol


matchDict dict c = 
          where (front, rest) = splitAt 4 c
                words = filter (\w -> length w == length front) dict



dist :: Eq a => [a] -> [a] -> Int
dist a b = last (if lab == 0 then mainDiag else if lab > 0 then lowers !! (lab - 1) else {- < 0 -} uppers !! (-1 - lab))
    where mainDiag = oneDiag a b (head uppers) (-1 : head lowers)
          uppers = eachDiag a b (mainDiag : uppers) -- upper diagonals
          lowers = eachDiag b a (mainDiag : lowers) -- lower diagonals
          lab = length a - length b

eachDiag a [] diags = []
eachDiag a (bch:bs) (lastDiag:diags) = oneDiag a bs nextDiag lastDiag : eachDiag a bs diags
         where nextDiag = head (tail diags)

oneDiag a b diagAbove diagBelow = thisdiag
        where firstelt = 1 + head diagBelow
              thisdiag = firstelt : doDiag a b firstelt diagAbove (tail diagBelow)

doDiag [] b nw n w = []
doDiag a [] nw n w = []
doDiag (ach:as) (bch:bs) nw n w = me : (doDiag as bs me (tail n) (tail w))
       where me = if ach == bch then nw else 1 + min3 (head w) nw (head n)
             min3 x y z = if x < y then x else min y z

toInt :: String -> [Int]
toInt = map read . words 
