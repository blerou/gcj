import Data.List (sort, nub, (\\))

data Lawn = Lawn {
     getRowNum :: Int,
     getColNum :: Int,
     getRows   :: [Int],
     getCols   :: [Int],
     squares   :: [((Int,Int),Int)]
} deriving (Show)

sample = unlines ["2", "3 3", "2 1 2", "1 1 1", "2 1 2", "1 3" ,"1 2 1"]

main = interact solve

solve = unlines . showCases . solveCases . parseCases . drop 1 . lines

parseCases cases = reverse $ parseCases' [] cases

solveCases lawns = reverse $ solveCases' [] lawns

showCases = zipWith renderer [1..] 
          where renderer i c = "Case #" ++ show i ++ ": " ++ c


parseCases' acc []    = acc
parseCases' acc cases = parseCases' (lawn : acc) (drop rows $ tail cases)
          where lawn = Lawn rows cols [0..rows-1] [0..cols-1] sqares
                [rows, cols] = toInt $ head cases
                sqares = concat $ convert $ map toInt $ take rows $ tail cases
                convert c = zipWith pairCols [0..] c
                pairCols i row = zipWith (\j sq -> ((i,j),sq)) [0..] row

toInt :: String -> [Int]
toInt = map read . words

solveCases' acc []           = acc
solveCases' acc (lawn:lawns) = solveCases' (result : acc) lawns
            where result = step sortedH lawn
                  sortedH = reverse $ sort $ nub $ map snd $ squares lawn

step []     lawn = "YES"
step (h:hs) lawn = if isHeightMowable then step hs newLawn else "NO"
     where mowables = mowableCells lawn
           heightCells = map fst $ filter (\(_, h') -> h' == h) $ squares lawn
           isHeightMowable = null $ heightCells \\ mowables
           newLawn = lawn { getRows = newRows, getCols = newCols }
           newRows = getRows lawn \\ map fst heightCells
           newCols = getCols lawn \\ map snd heightCells
           

mowableCells lawn = nub $ mowableInRows lawn ++ mowableInCols lawn
mowableInRows lawn = concat $ map (\rowNum -> zip (repeat rowNum) row) rows
              where row = [0.. getColNum lawn - 1]
                    rows = getRows lawn

mowableInCols lawn = concat $ map (\colNum -> zip col (repeat colNum)) cols
              where col = [0.. getRowNum lawn - 1]
                    cols = getCols lawn
