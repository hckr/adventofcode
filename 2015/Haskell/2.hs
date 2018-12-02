import Data.List

replace :: Char -> Char -> Char -> Char
replace a b c | c == a    = b
              | otherwise = c

extractDimensions :: [Char] -> [Int]
extractDimensions line = read ("[" ++ (map (replace 'x' ',') line) ++ "]")

countNeededWrappingPaperArea :: [Int] -> Int
countNeededWrappingPaperArea [a, b, c] =
    side1 * 2 + side2 * 2 + side3 * 2 + minimum [side1, side2, side3] where
        side1 = a * b
        side2 = a * c
        side3 = b * c

countNeededRibbonLength :: [Int] -> Int
countNeededRibbonLength dimensions = shortestDistanceAroundSides + bow where
    shortestDistanceAroundSides = (sum $ take 2 $ sort dimensions) * 2
    bow = product dimensions

main = do
    input <- readFile "../2.in"
    let listOfDimensions = map extractDimensions (lines input)
    print $ sum $ map countNeededWrappingPaperArea listOfDimensions
    print $ sum $ map countNeededRibbonLength listOfDimensions
