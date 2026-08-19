class NumberRange:
    min_value: int
    max_value: int

    def __init__(self, min_value: int, max_value: int):
        if min_value < 0 or max_value < 0:
            raise Exception('The NumberRange must consist of positive values!')
        if min_value > max_value:
            raise Exception('The number of min_value must be less than or equal to max_value!')
        self.min_value = min_value
        self.max_value = max_value

def get_lowest_common_multiple(number_range: NumberRange):
    lcm = number_range.max_value
    while lcm % number_range.min_value != 0:
        lcm += number_range.max_value
    return lcm

print(get_lowest_common_multiple(NumberRange(5, 7)))
print(get_lowest_common_multiple(NumberRange(23, 45)))

"""
Algorithmenanalyse:
    - lcm = numberRange.max_value (Zeile 14) wird genau einmal ausgeführt -> O(1)
    - Die while-Schleife (Zeile 15) wird solange ausgeführt, bis ein Vielfaches von max_value gefunden wird, das durch min_value teilbar ist 
    - In jedem Schleifendurchlauf werden nur konstante viele Operationen ausgeführt:
        > Eine Modulo-Operation mit einem Vergleich mit O
        > Inkrementierung von lcm mit max_value
    - Anzahl Schleifendurchläufe enspricht der Anzahl der geprüften Vielfachen von max_value
        > kgV(min_value, max_value) / max_value - 1 (die Schleife startet direkt mit dem ersten Vielfachen von max_value)
        > daraus folgt: kgV(min_value, max_value) = (min_value * max_value) / ggT(min_value, max_value)
        => Anzahl an Schleifendurchläufen = (a / ggT(min_value, max_value)) - 1
    - Schlimmstmöglicher Fall:
        > min_value und max_value haben einen größten gemeinsamen Teiler von 1 -> ggT(min_value, max_value) = 1
        => Anzahl an Schleifendurchläufen = a - 1 
           
    Ergebnis:
    - T(min_value) = c1 + c2 · min_value
    - Da Konstanten in der O-Notation vernachlässigt werden, ergibt sich:
      T(min_value) = O(min_value)
    - Mit n = min_value folgt:
      T(n) = O(n)
"""