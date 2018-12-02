import Data.Set (Set)
import qualified Data.Set as Set

instructionToCoordinates :: Char -> [Int]
instructionToCoordinates ins | ins == '^'  = [-1,  0]
                             | ins == '>'  = [ 0,  1]
                             | ins == 'v'  = [ 1,  0]
                             | ins == '<'  = [ 0, -1]
                             | otherwise   = [ 0,  0]

move :: [Int] -> [Int] -> [Int]
move position coordinates = zipWith (+) position coordinates

collectVisitedHouses :: [Int] -> [[Int]] -> Set [Int]
collectVisitedHouses startingPos = iter (Set.singleton startingPos) startingPos where
    iter visitedHouses position (direction:restCoordinates) =
        iter (Set.insert newCoord visitedHouses) newCoord restCoordinates where
            newCoord = move position direction
    iter visitedHouses _ [] = visitedHouses

getVisitedHouses :: [[Int]] -> Set [Int]
getVisitedHouses listOfCoordinates = collectVisitedHouses [0, 0] listOfCoordinates

everyNth :: Int -> [a] -> [a]
everyNth n (x:xs) = x : (everyNth n xd) where
    xd = drop (n-1) xs
everyNth _ [] = []

main = do
    input <- getContents
    let listOfCoordinates = map instructionToCoordinates input
    print $ length $ getVisitedHouses listOfCoordinates
    let santasList = everyNth 2 listOfCoordinates
    let robosantasList = everyNth 2 (tail listOfCoordinates)
    print $ length ( Set.union (getVisitedHouses santasList) (getVisitedHouses robosantasList) )
