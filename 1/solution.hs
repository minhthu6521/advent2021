wordsWhen     :: (Char -> Bool) -> String -> [String]
wordsWhen p s =  case dropWhile p s of
                      "" -> []
                      s' -> w : wordsWhen p s''
                            where (w, s'') = break p s

splitToInt :: String ->  [String]
splitToInt x = words x

readInt :: String -> Int
readInt = read

main = do
    s <- readFile "input.txt"
    print (wordsWhen (=='\n') s)