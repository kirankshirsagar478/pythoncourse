dict={
    "Prakash":"light",
    "Paus":"rain",
    "Manjar":"cat"
}
print (dict.keys())
a=input("Enter the word:")
# print("meaning of the word:",dict[a])    --> it throws an error when wrong word is entered
#solution for error
print("meaning of the word:",dict.get(a))