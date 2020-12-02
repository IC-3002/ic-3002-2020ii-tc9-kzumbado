def quicksort(n):

    size = len(n)
    menores = []
    mayores = []

    if size == 1 or size == 0:
        return n

    else:
        pivote = n[(size - 1) // 2]
        pivoteComp = n[(size - 1) // 2][1]
        for j in range(size):
            if n[j][1] < pivoteComp:
                menores.append(n[j])
            elif n[j][1] > pivoteComp:
                mayores.append(n[j])
        
        menores = quicksort(menores)
        mayores = quicksort(mayores)
        menores.append(pivote)

        return menores + mayores

def maximizar(As, D):
    As= quicksort(As)
    actValor= 0
    result = []
    for i in range (0, len(As)):
        if (actValor + As[i][1]) <= D:
            result += [As[i]]
            actValor += As[i][1]
    return result
