class NumberRange:
    minValue: int
    maxValue: int

    def __init__(self, minValue: int, maxValue: int):
        if minValue < 0 or maxValue < 0:
            raise Exception('The NumberRange must consist of positive values!')
        if minValue > maxValue:
            raise Exception('The number of minValue must be less than or equal to maxValue!')
        self.minValue = minValue
        self.maxValue = maxValue

def getLowestCommonMultiple(numberRange: NumberRange):
    lcm = numberRange.maxValue
    while lcm % numberRange.minValue != 0:
        lcm += numberRange.maxValue
    return lcm

print(getLowestCommonMultiple(NumberRange(5, 7)))
print(getLowestCommonMultiple(NumberRange(23, 45)))

"""
Algorithmenanalyse:
    - lcm = numberRange.maxValue (Zeile 14) wird genau einmal ausgeführt -> O(1)
    - Die while-Schleife (Zeile 15) wird solange ausgeführt, bis ein Vielfaches von maxValue gefunden wird, das durch minValue teilbar ist 
    - In jedem Schleifendurchlauf werden nur konstante viele Operationen ausgeführt:
        > Eine Modulo-Operation mit einem Vergleich mit O
        > Inkrementierung von lcm mit maxValue
    - Anzahl Schleifendurchläufe enspricht der Anzahl der geprüften Vielfachen von maxValue
        > kgV(minValue, maxValue) / maxValue - 1 (die Schleife startet direkt mit dem ersten Vielfachen von maxValue)
        > daraus folgt: kgV(minValue, maxValue) = (minValue * maxValue) / ggT(minValue, maxValue)
        => Anzahl an Schleifendurchläufen = (a / ggT(minValue, maxValue)) - 1
    - Schlimmstmöglicher Fall:
        > minValue und maxValue haben einen größten gemeinsamen Teiler von 1 -> ggT(minValue, maxValue) = 1
        => Anzahl an Schleifendurchläufen = a - 1 
           
    Ergebnis:
    - T(minValue) = c1 + c2 · minValue
    - Da Konstanten in der O-Notation vernachlässigt werden, ergibt sich:
      T(minValue) = O(minValue)
    - Mit n = minValue folgt:
      T(n) = O(n)
"""