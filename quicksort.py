# putting the pivot in the right place
def partition(arr, pvot):
    
    rigthPointer = len(arr)-1
    leftPointer = 1
    
    while True:
        
        # move the right pointer until the conflict is reached
        while arr[rigthPointer] >= pvot and rigthPointer >= leftPointer:
            rigthPointer -= 1
            
        # move the left pointer until the conflict is reached
        while arr[leftPointer] < pvot and rigthPointer >= leftPointer:
            leftPointer += 1
            #left pointer is end of the arry
            if leftPointer > len(arr)-1:
                break
        
        #we are in pivot right place 
        if leftPointer > rigthPointer:
            break 
        #swap pointers
        else:
            arr[leftPointer], arr[rigthPointer] = arr[rigthPointer], arr[leftPointer]
    
    #place pivot
    arr[0] , arr[rigthPointer] = arr[rigthPointer], arr[0]
    
    #return patitions
    return arr[:rigthPointer], arr[rigthPointer+1:]
    
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    #we take the left number as a pivot
    pvot = arr[0]
    p1 , p2 = partition(arr, pvot)
    
    return quicksort(p1) + [pvot] + quicksort(p2)

A = [7,4,6,9,5,10,1,4]
A = quicksort(A)
print(A)