data Robot = O | B deriving (Read, Show)
type Pos = Int
data Result = Result { lastPosO :: Pos, bufferO :: Int, lastPosB :: Pos, bufferB :: Int, aggr :: Int} deriving (Show)

main = do
  cases <- getContents
  putStr $ unlines . solve . (drop 1) . lines $ cases

solve :: [String] -> [String]
solve cases = 
  let results = map (botTrust . parse) cases
  in zipWith (\i result -> "Case #" ++ show i ++ ": " ++ format result) [1..] results

parse :: String -> [(Robot, Pos)]
parse line = parseParts . (drop 1) . words $ line 
parseParts :: [String] -> [(Robot, Pos)]
parseParts [] = []
parseParts (robot:pos:ps) = (read robot, read pos):parseParts ps

botTrust :: [(Robot, Pos)] -> Result
botTrust seq = foldl foldSteps (Result 1 0 1 0 0) seq
foldSteps :: Result -> (Robot, Pos) -> Result
foldSteps result (O, pos) = 
  let distance = abs (pos - lastPosO result) + 1
      buffer = bufferO result
      steps = if distance > buffer then distance - buffer else 1
  in Result pos 0 (lastPosB result) (bufferB result + steps) (aggr result + steps)
foldSteps result (B, pos) =
  let distance = abs (pos - lastPosB result) + 1
      buffer = bufferB result
      steps = if distance > buffer then distance - buffer else 1
  in Result (lastPosO result) (bufferO result + steps) pos 0 (aggr result + steps)

format :: Result -> String
format result = show $ aggr result
