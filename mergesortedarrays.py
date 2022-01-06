#mergeSortedArrays([0, 3,4,31], [4,6,40])

def mergeSortedArray(arr1, arr2):
    mergedArray = []
    i=0
    j=0

    if len(arr1) == 0:
        return arr2
    elif len(arr2) == 0:
        return arr1

    while(i<len(arr1) and j<len(arr2)):
        if arr1[i] < arr2[j]:
            mergedArray.append(arr1[i])
            i+=1
        else:
            mergedArray.append(arr2[j])
            j+=1
        
    while(i<len(arr1)):
        mergedArray.append(arr1[i])
        i+=1
        
    while (j<len(arr2)):
        mergedArray.append(arr2[j])
        j+=1    
    return mergedArray
    
a=[1,3,4,6,20,35]
b=[2,3,4,5,6,9,11,98]

print(mergeSortedArray(a,b))


