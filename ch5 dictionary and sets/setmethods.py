a={3,2,6,9,7,8}
print(a)
#adding elements
a.add(4)
a.add(5)
a.add(5) #doesn't matter
a.add((0)) #can add only tuples
print(a)
# a.add([1]) #we can't add list into set
# a.add({"kiran":"good boy"}) #we can't add dictionary into set
#length of the set
print(len(a)) #prints lenght of the set
#remove
a.remove(0)
print (a)
#pop
print(a.pop()) #pics random value and remove it
print(a)
