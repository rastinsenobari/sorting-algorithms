
def selectionsort(arry):
    
    n = len(arry)
    
    for i in range(n):
        #position of minimum > for begin, first number
        p_min =  i
         
        for j in range(i, n):
            if arry[j] < arry[p_min]:
                p_min = j
                        
        arry[i], arry[p_min] = arry[p_min], arry[i]
    
    return arry
            
A = [7,4,6,9,5,10,1,4]
A = selectionsort(A)
print(A)