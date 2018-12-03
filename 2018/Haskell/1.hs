import Data.Set (Set)
import qualified Data.Set as Set

toInt :: [Char] -> Int
toInt ('+':xs) = read xs
toInt      xs  = read xs

firstSameFrequency :: [Int] -> Int
firstSameFrequency changes = iter 0 Set.empty (cycle changes) where
    iter frequency previousFrequencies (c:cs) =
        if Set.member newFrequency previousFrequencies then
            newFrequency
        else
            iter newFrequency (Set.insert newFrequency previousFrequencies) cs
        where
            newFrequency = frequency + c

main = do
    input <- getContents
    let changes = (map toInt (lines input))
    print $ sum changes
    print $ firstSameFrequency changes
