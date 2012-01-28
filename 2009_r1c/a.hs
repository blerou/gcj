solve :: String -> Int
solve input = conv (assoc [] input)

assoc :: String -> String -> [Int]
assoc _ [] = []
assoc alloc (x:input)
	| x `elem` alloc = 
		let	xi = (x `indexOf` alloc)
		in xi : assoc alloc input
	| otherwise = 
		let	xi = (length alloc)
		in xi : assoc (alloc ++ [x]) input
	where
		x `indexOf` (h:a)
			| x == h	= 0
			| otherwise	= 1 + (x `indexOf` a)

conv :: [Int] -> Int 
conv idx = conv' base 0 (rewrite idx)
	where
		base = 1 + (max' idx)
		max' [x] = x
		max' (x:xs)
			| x > mt = x
			| otherwise = mt
			where mt = max' xs
		rewrite [] = []
		rewrite (1:xs) = (rewrite xs) ++ [0]
		rewrite (0:xs) = (rewrite xs) ++ [1]
		rewrite (x:xs) = (rewrite xs) ++ [x]
		conv' _ _ [] = 0
		conv' base pos (x:xs) = (base^pos) * x + (conv' base (pos + 1) xs)
