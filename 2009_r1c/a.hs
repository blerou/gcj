solve :: String -> Int
solve testCase = conv_to_ten (vals [] testCase)

vals :: String -> String -> [Int]
vals _ [] = []
vals alloc (x:testCase)
  | x `elem` alloc = let xi = (x `indexOf` alloc)
                     in xi : vals alloc testCase
  | otherwise = let xi = (length alloc) 
                in xi : vals (alloc ++ [x]) testCase
      where x `indexOf` (h:a)
              | x == h = 0
              | otherwise = 1 + (x `indexOf` a)

conv_to_ten :: [Int] -> Int 
conv_to_ten vals = conv_to_ten' base 0 (reverse (rearrangeVals vals))
  where base = 1 + (max' vals)
        max' [x] = x
	max' (x:xs)
          | x > mt = x
          | otherwise = mt
            where mt = max' xs
        rearrangeVals [] = []
        rearrangeVals (1:xs) = 0:(rearrangeVals xs)
        rearrangeVals (0:xs) = 1:(rearrangeVals xs)
        rearrangeVals (x:xs) = x:(rearrangeVals xs)
        conv_to_ten' _ _ [] = 0              
        conv_to_ten' base exp (x:xs) = (base^exp) * x + (conv_to_ten' base (exp + 1) xs)
