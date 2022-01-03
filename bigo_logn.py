import time

fish = ['dory', 'bruce' , 'marlin', 'nemo']

nemo = ['nemo']

everyone = ['dory', 'bruce' , 'marlin', 'nemo', 'gill', 'bloat', 'nigel', 'darla', 'hank']

large = ['nemo' for i in range(10)]

def findNemo2(fish):
    t0 = time.time()
    for i in range(0, len(fish)):
        if (fish[i] == 'nemo'):
            print('found nemo ...')
    t1 = time.time()

    print(f'finding nemo took {t1-t0} seconds')

findNemo2(everyone)


