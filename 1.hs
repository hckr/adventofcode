convertChar :: Char -> Int
convertChar '(' = 1
convertChar _ = -1

convertString :: [Char] -> [Int]
convertString = map convertChar

countFloor :: [Int] -> Int
countFloor = foldl (+) 0

instructionNrToEnterBasement :: [Int] -> Int
instructionNrToEnterBasement = iter 1 0 where
    iter nr level (x:xs) =
        if newLevel == -1 then
            nr
        else
            iter (nr+1) newLevel xs
        where newLevel = level + x

main = do
    input <- readFile "1.in"
    let instructions = convertString input
    print $ countFloor $ instructions
    print $ instructionNrToEnterBasement $ instructions
