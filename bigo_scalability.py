import time

myarr = ['nemo']
mynewlist = ['nemo' for i in range(10000)]

def myfunc (myarr):
    t0 = time.time()    
    for i in myarr:
        if (i == 'nemo'):
            print('found Nemo')
    t1 = time.time() - t0
    print(f"call to find nemo took {t1} seconds")


myfunc(mynewlist)


