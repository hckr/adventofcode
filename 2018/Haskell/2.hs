import Data.Map.Strict as Map
import qualified Data.Map.Strict as Map
import qualified Data.List as List
import Data.Maybe

countChars :: [Char] -> Map Char Int
countChars = iter (Map.empty) where
    iter :: Map Char Int -> [Char] -> Map Char Int
    iter counts [] = counts
    iter counts (c:cs) = iter (Map.insertWithKey f c 1 counts) cs where
        f key new_value old_value = old_value + new_value

hasDoubles :: [Char] -> Bool
hasDoubles = elem 2 . Map.elems . countChars

hasTriples :: [Char] -> Bool
hasTriples = elem 3 . Map.elems . countChars

computeHash :: [[Char]] -> Int
computeHash = iter 0 0 where
    iter :: Int -> Int -> [[Char]] -> Int
    iter doubles triples [] = doubles * triples
    iter doubles triples (boxId:boxIds) = iter newDoubles newTriples boxIds where
        incIf val True  = val + 1
        incIf val False = val
        newDoubles = doubles `incIf` (hasDoubles boxId)
        newTriples = triples `incIf` (hasTriples boxId)

findOnlyDifferencePos :: [Char] -> [Char] -> Maybe Int
findOnlyDifferencePos = iter 0 0 0 where
    iter pos diffs _ [] _ | diffs > 1 = Nothing
    iter pos 1 lastdiff [] _ = Just lastdiff
    iter pos diffs lastdiff (a:as) (b:bs) | a == b    = iter (pos+1) diffs lastdiff as bs
                                          | otherwise = iter (pos+1) (diffs+1) pos as bs
    iter _ _ _ _ _ = Nothing

findMachingBoxCommonLetters :: [[Char]] -> [Char] -> Maybe [Char]
findMachingBoxCommonLetters = iter where
    iter (bId:boxIds) boxId = case findOnlyDifferencePos bId boxId of
        Just diff -> return ((List.take diff boxId) ++ (List.drop (diff+1) boxId))
        Nothing -> iter boxIds boxId
    iter [] _ = Nothing

findMachingBoxesCommonLetters :: [[Char]] -> Maybe [Char]
findMachingBoxesCommonLetters = iter where
    iter (bId:boxIds) = case findMachingBoxCommonLetters boxIds bId of
        Just common -> return common
        Nothing -> iter boxIds

main = do
    input <- getContents
    let boxIds = lines input
    print $ computeHash boxIds
    putStrLn $ fromMaybe "not found" (findMachingBoxesCommonLetters boxIds)
