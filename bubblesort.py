# Creating a bubble sort function
def bubble_sort(mylist):
    for i in range(0, len(mylist)-1):
        for j in range(len(mylist)-1):
            if mylist[j] > mylist[j+1]:
                temp = mylist[j]
                mylist[j] = mylist[j+1]
                mylist[j+1] = temp
    return mylist


mylist = [5, 3, 8, 6, 7, 2]
print("The unsorted list is: ", mylist)
# Calling the bubble sort function
print("The sorted list is: ", bubble_sort(mylist))
