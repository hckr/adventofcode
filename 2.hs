replace :: Char -> Char -> Char -> Char
replace a b c | c == a    = b
              | otherwise = c

deleteFirst :: (Eq a) => a -> [a] -> [a]
deleteFirst = iter [] where
    iter result _ [] = result
    iter result elem (x:xs) =
        if elem == x then
            result ++ xs
        else
            iter (result ++ [x]) elem xs

extractDimensions :: [Char] -> [Int]
extractDimensions line = read ("[" ++ (map (replace 'x' ',') line) ++ "]")

countNeededWrappingPaperArea :: [Int] -> Int
countNeededWrappingPaperArea [a, b, c] =
    side1 * 2 + side2 * 2 + side3 * 2 + minimum [side1, side2, side3] where
        side1 = a * b
        side2 = a * c
        side3 = b * c

accumulateNeededWrappingPaperArea :: Int -> [Char] -> Int
accumulateNeededWrappingPaperArea acc line = acc + (countNeededWrappingPaperArea . extractDimensions) line

countNeededRibbonLength :: [Int] -> Int
countNeededRibbonLength list =
    foldl (+) 0 (map (*2) (deleteFirst (maximum list) list)) + foldl (*) 1 list

accumulateNeededRibbonLength :: Int -> [Char] -> Int
accumulateNeededRibbonLength acc line = acc + (countNeededRibbonLength . extractDimensions) line

main = do
    input <- readFile "2.in"
    print $ foldl accumulateNeededWrappingPaperArea 0 (lines input)
    print $ foldl accumulateNeededRibbonLength 0 (lines input)