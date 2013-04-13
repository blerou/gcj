import Data.List
import Text.Printf

main = do
  cases <- getContents
  putStr $ unlines . solve . drop 1 . lines $ cases

solve :: [String] -> [String]
solve cases = zipWith (\i r -> "Case #" ++ show i ++ ":" ++ format r) [1..] results
  where results = map (safetyNumbers . parse) cases 

parse :: String -> [Int]
parse = tail . map read . words

safetyNumbers :: [Int] -> [Double]
safetyNumbers scores = map snd $ sort $ map swapDone done ++ map minVotes remaining
  where 
    scoreSum = fromIntegral $ sum scores
    allAvg = scoreSum / (fromIntegral $ length scores)
    (done, remaining) = partition (\(s, _) -> s >= allAvg * 2) $ zip (map fromIntegral scores) [1..]
    remSum = scoreSum * 2 - foldl (\sum (n, _) -> sum + n) 0 done
    remAvg = remSum / (fromIntegral $ length remaining)
    minVotes (n,i) = (i, (remAvg - n) / scoreSum)
    swapDone (n,i) = (i, 0)

format :: [Double] -> String
format = foldl (\res p -> res ++ printf " %.6f" (p*100)) ""
