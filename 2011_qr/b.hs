--solve testCase = solve' invokes combs opps
--  where (combs, opps, invokes) = parse testCase 

--parse testCase = []

solve' invokes combs opps = let c = prepComb combs
                                o = prepOpp opps
                            in apply' invokes c o []

prepComb :: [Char] -> [Char]
prepComb [] = []
prepComb (x:y:r:comb) = x:y:r:y:x:r:prepComb comb

prepOpp :: [Char] -> [Char]
prepOpp [] = []
prepOpp (x:y:opps) = x:y:y:x:prepOpp opps

apply' :: [Char] -> [Char] -> [Char] -> [Char] -> [Char]
apply' [] _ _ _ = []
apply' [i] _ _ _ = [i]
apply' (i1:i2:invokes) combs opps actOpps = case comb combs i1 i2 of
  Nothing -> i1:apply' (i2:invokes) combs opps actOpps
  Just r  -> r:apply' invokes combs opps actOpps

comb :: [Char] -> Char -> Char -> Maybe Char
comb [] _ _ = Nothing
comb (c1:c2:r:combs) i1 i2
  | i1 == c1 && i2 == c2 = Just r
  | otherwise = comb combs i1 i2

--opp :: [Char] -> 
