def bubblesort(arry):
    n = len(arry)
    for i in range(n):
        flag = True
        for j in range(0, n-i-1):
            if arry[j] > arry[j+1]:
                flag = False
                arry[j], arry[j+1] = arry[j+1], arry[j]
        #check the arry is sorted or no 
        if flag:
            break
    return arry

A = [7,4,6,9,5,10,1,4]

A = bubblesort(A)
print(A)