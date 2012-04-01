main = do
  cases <- getContents
  putStr $ unlines . solve . (drop 1) . lines $ cases

solve cases = 
  let results = map (magicka . parse) cases
  in zipWith (\i result -> "Case #" ++ show i ++ ": " ++ format result) [1..] results

parse :: String -> [String]
parse line = 
  let parts = words line
      numOfCombos = read $ head parts
      combos = prepareCombos $ concat $ take numOfCombos (tail parts)
      partsAfterCombos = drop numOfCombos (tail parts)
      numOfOpps = read $ head partsAfterCombos
      opps = concat $ take numOfOpps (tail partsAfterCombos)
      invokes = last parts
  in [invokes, opps, combos]
    where prepareCombos [] = []
          prepareCombos (c1:c2:r:xs) = c1:c2:r:c2:c1:r:prepareCombos xs

magicka :: [String] -> String
magicka (invokes:opps:combos:_) = reverse $ foldl (foldInvokes combos opps) [] invokes

foldInvokes :: String -> String -> String -> Char -> String
foldInvokes combos opps is i1 = applyOpp opps resolvedCombos
  where magicWord = i1:is
        resolvedCombos = applyCombo combos magicWord

applyCombo :: String -> String -> String
applyCombo _ [] = []
applyCombo (c1:c2:r:cs) i@(i1:i2:is)
  | isCombo   = r:is
  | otherwise = applyCombo cs i
    where isCombo = i1 == c1 && i2 == c2
applyCombo _ i = i

applyOpp :: String -> String -> String
applyOpp [] i = i
applyOpp (o1:o2:os) i
  | o1 `elem` i && o2 `elem` i = []
  | otherwise                  = applyOpp os i

format :: String -> String
format res = '[' : (normResult $ foldr formatResult "]" res)
  where formatResult ch acc = ", " ++ [ch] ++ acc
        normResult res
          | length res > 1 = tail $ tail res
          | otherwise      = "]"
