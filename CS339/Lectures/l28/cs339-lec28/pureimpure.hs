name2reply :: String -> String
name2reply name = "Welcome again, " ++ name ++ ".\n" ++
                  "Your name contains " ++ charCount ++ " characters."
                      where charCount = show (length name)

main :: IO ()
main = do
        putStrLn ("Greetings! What is your name?")
        inpStr <- getLine
        putStrLn (name2reply inpStr)
