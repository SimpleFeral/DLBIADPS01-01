calcSumOfSquaresRec n = if n <= 0 
    then 0
    else (n*n) + calcSumOfSquaresRec (n-1)  

calcSumOfSquaresDec n = sum [x^2 | x <- [1..n]]

main = do
    print $ calcSumOfSquaresRec 4
    print $ calcSumOfSquaresDec 4