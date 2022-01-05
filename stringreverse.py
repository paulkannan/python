def reverse(mystr):
    #check for inputs
    if (len(mystr)==0 or type(mystr)!=str):
        return "This was not expected"

    #reverse the string
    mylist=[]
    for word in range(len(mystr)-1,-1,-1):
        mylist.append(mystr[word])
    return ''.join(mylist)


mystring= "My name is Paul"

print(reverse(mystring))