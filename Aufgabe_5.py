def isSortedAsc(numList):
    list_length = len(numList)
    
    if list_length <= 1:
        return True
    
    for i in range(0, list_length-1):
        if numList[i] > numList[i+1]:
            return False
    
    return True

'''
## Beweis der Korrektheit durch mathematische Induktion ##

Es gilt zu zeigen, dass die Funktion isSortedAsc genau dann True 
zurückgibt, wenn die List numList aufsteigend sortiert ist

1. Induktionsanfang (n=1):
    > Eine Liste mit genau einem Element ist sortiert, da keine Wertpaare 
      für den Vergleich existieren und somit die Sortierung nicht verletzt 
      werden könnte
    > Für eine Liste der Länge 1 gilt:
      listLength <= 1
    > Somit wird sofort folgende Anweisung ausgeführt:
      return True
    => Damit liefert die Funktion für n=1 das korrekte Ergebnis.

2. Induktionsvoraussetzung/Induktionsannahme:
    > Es existiert ein beliebiges n ∈ ℕ, so dass die Funktion 
      für jede Liste der Länge n korrekt auswertet, 
      ob diese aufsteigend sortiert ist. 
      
2. Induktionsschritt (n=1 -> n=1+k):
    > Zu zeigen ist, dass die Funktion auch für eine Liste 
      mit der Länge n+1 das korrekte Ergebnis auswertet.

    > Die Schleife 
         for i in range(0, listLength-1)
      vergleicht wiederholt jedes Element mit seinem direkten Nachfolger.
    
    > Fall 1:
        Es existiert ein Index i mit
            numList[i] > numList[i+1]
        Somit liegt eine Verletzung der Sortierung vor, weshalb die Anweisung 
            return False 
        ausgeführt und die Liste korrekt als unsortiert ausgewertet wird.
    
    > Fall 2:
        Für alle Indizes i gilt
            numList[i] ≤ numList[i+1]
        Damit ist jedes Element ≤ seinem direkten Nachfolger, die Schleife 
        wird vollständig durchlaufen und die Funktion führt die Anweisung
            return True
        aus. Damit erfüllt die Liste die Definition einer aufsteigend 
        sortierter Liste und Funktion wertet die Liste als korrekt sortiert aus.
'''
