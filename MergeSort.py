def mergesort (arr):
    if len(arr) < 2:
        return arr
    mid = len (arr) // 2
    B = arr[:mid]
    C = arr[mid:]

    B = mergesort(B)
    C = mergesort(C)
    
    i = j = 0
    arr = [ ]
    while i < len(B) and j < len(C):
        if B[i] <= C[j]:
            arr.append(B[i])
            i += 1
        else:
            arr.append(C[j])
            j += 1
            
    # if there is a number left in B or C
    arr += B[i:] + C[j:]
    
    return arr

A = [7,4,6,9,5,10,1,4]
A = mergesort(A)
print(A)