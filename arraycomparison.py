import time
myarr2 = ['a', 'b', 'c', 's']
myarr1 = ['z','y', 'x']

def compare_arrays(arr1, arr2):
    t0 = time.time()

    for i in range(0,len(arr1)):
        for j in range(0,len(arr2)):
            if arr1[i]==arr2[j]:
                return True
    t1 = time.time()
    print(f'program took {t1-t0} seconds ')
    return False
           
def compare_arrays_bestway(arr1, arr2):
    t0 = time.time()
    mymap = {k:'true' for k in (arr2)}
    
    for i in range(0,len(arr1)):
        if arr1[i] in mymap.keys():
            return True
    t1 = time.time()
    print(f'program took {t1-t0} seconds ')        
    return False
        

print(compare_arrays(myarr1, myarr2))
print(compare_arrays_bestway(myarr1, myarr2))
