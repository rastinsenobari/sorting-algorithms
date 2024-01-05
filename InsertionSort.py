def insertionsort(arry):
    n = len(arry)
    for i in range(1,n):
        pvot = arry[i]
        j = i
        while arry[j-1] > pvot and j > 0:
            arry[j] = arry[j-1]
            j -= 1
        arry[j] = pvot

    return arry

A = [7,4,6,9,5,10,1,4]
A = insertionsort(A)
print(A)