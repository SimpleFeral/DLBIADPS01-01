import tracemalloc
import inspect
import sys
from memory_profiler import profile

@profile
def calc_faculty_recursive(n: int):
    """
    Diese Funktion berechnet rekursiv die Fakultät einer positiven Ganzzahl. \n
    Sie verfügt über eine Abbruchbedingung, um die Rekursion zu beenden (Basisfall), \n
    sobald der Wert des übergebenen Parameters 0 oder 1 ist.

    Args:
        n (int): Positive Ganzzahl, für welche die Fakultät berechnet werden soll.

    Returns:
        result (int): Das Produkt aller Zahlen von 1 bis n.
    """
    
    # Rekursionstiefe ausgeben
    print('Current stack depth:', len(inspect.stack())) 
    
    # Analyse des Heap-Speichers
    traced_memory = tracemalloc.get_traced_memory()
    print('Current heap size:', traced_memory[0])
    print('Maximum heap size:', traced_memory[1])
    
    print()
    
    # Abbruchbedingung
    if n <= 1:
        return 1
    return n * calc_faculty_recursive(n-1)
    

@profile
def calc_faculty(n: int):
    """
    Diese Funktion berechnet iterativ die Fakultät einer positiven Ganzzahl. \n
    Solange i < n+1 ist, wird das Ergebnis mit dem aktuellen Wert von n multipliziert.

    Args:
        n (int): Positive Ganzzahl, für welche die Fakultät berechnet werden soll.

    Returns:
        result (int): Das Produkt aller Zahlen von 1 bis n.
    """
    result = 1
    for i in range(1, n + 1):
        
        # Rekursionstiefe ausgeben
        print('Current stack depth:', len(inspect.stack())) 
           
        # Analyse des Heap-Speichers
        traced_memory = tracemalloc.get_traced_memory()
        print('Current heap size:', traced_memory[0])
        print('Maximum heap size:', traced_memory[1])
           
        print()
        
        result *= i
    return result

tracemalloc.start()

n = 30

try:
    print(f'Computed faculty with recursion of {n}:', calc_faculty_recursive(n))
except RecursionError:
    recusion_limt = sys.getrecursionlimit()
    print(f'{n} exeeds the recursion limit of {recusion_limt}. Please choose a value less than {recusion_limt} for compution of the facultity or use the iterative function instead.')
print('\n')
print(f'Computed faculty with iteration of {n}:', calc_faculty(n))

tracemalloc.stop()
