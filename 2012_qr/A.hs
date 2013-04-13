import Data.List
import qualified Data.Map as M

type GoogMap = (Char, Char)

main = interact $ unlines . solve . tail . lines

solve :: [String] -> [String]
solve cases = 
  let results = solveCase (buildDict sample) cases
  in zipWith (\i r -> "Case #" ++ show i ++ ": " ++ format r) [1..] results
  where sample = [
          ("ejp mysljylc kd kxveddknmc re jsicpdrysi", "our language is impossible to understand"),
          ("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "there are twenty six factorial possibilities"),
          ("de kr kd eoya kw aej tysr re ujdr lkgc jv", "so it is okay if you want to just give up")]

buildDict :: [(String, String)] -> [GoogMap]
buildDict [] = []
buildDict ((goog,eng):xs) = nub $ defaultMap ++ rawMap
  where rawMap = (resolveTrans goog eng) ++ buildDict xs
        defaultMap = [('y', 'a'), ('e', 'o'), ('q', 'z'), ('z', 'q')]

resolveTrans :: String -> String -> [GoogMap]
resolveTrans goog eng = zipWith (\g e -> (g, e)) goog eng

solveCase :: [GoogMap] -> [String] -> [String]
solveCase dict [] = []
solveCase dict (goog:xs) = translate goog dict : solveCase dict xs

translate :: String -> [GoogMap] -> String
translate goog dict = map transFunc goog
  where transFunc g = resFunc $ M.lookup g $ M.fromList dict
        resFunc (Just x) = x

format = id
