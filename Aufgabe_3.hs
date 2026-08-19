calcSumOfSquares n = if n <= 1
                      then 1 
                      else (n*n) + calcSumOfSquares(n-1)
main = do
print $ calcSumOfSquares(4)