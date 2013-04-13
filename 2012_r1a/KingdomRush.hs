import Data.List

data LevelDesc = Ld Int Int Bool deriving (Show, Eq)
type Levels = [LevelDesc]

main = do
  cases <- getContents
  putStr $ unlines . solve . drop 1 . lines $ cases

solve :: [String] -> [String]
solve cases = zipWith (\i r -> "Case #" ++ show i ++ ": " ++ format r) [1..] results
  where results = solveCase cases
  
solveCase :: [String] -> [Int]
solveCase [] = []
solveCase (n:cases) = kingdomRush 0 0 levels : solveCase (drop levelCount cases)
  where levelCount = read n :: Int
        levels = map parse $ take levelCount cases

parse :: String -> LevelDesc
parse line = Ld s1 s2 False
  where [s1, s2] = map read . words $ line

kingdomRush :: Int -> Int -> Levels -> Int
kingdomRush _ plays []         = plays
kingdomRush stars plays levels = 
  if any completable levels
  then kingdomRush nextStars nextPlays uncompleted
  else useNextPossible stars plays levels
  where completable (Ld _ req2stars _) = req2stars <= stars
        (completed, uncompleted) = partition completable levels
        nextStars = foldl (\sum (Ld _ _ played) -> sum + (if played then 1 else 2)) stars completed
        nextPlays = plays + length completed

useNextPossible :: Int -> Int -> Levels -> Int
useNextPossible stars plays uncompleted =
  if any possibleFrom uncompleted
  then kingdomRush (stars+1) (plays+1) (swapPlayed uncompleted next)
  else 0
  where
    possibleFrom (Ld req1star _ played) = req1star <= stars && not played
    next = findBest $ filter possibleFrom uncompleted

findBest :: Levels -> LevelDesc
findBest (l:ls) = foldl findBestFunc l ls
  where findBestFunc best@(Ld _ best2s _) l@(Ld _ l2s _) = if l2s > best2s then l else best

swapPlayed :: Levels -> LevelDesc -> Levels
swapPlayed uncompleted best@(Ld s1 s2 _) = Ld s1 s2 True : delete best uncompleted

format :: Int -> String
format r = if r == 0 then "Too bad" else show r
