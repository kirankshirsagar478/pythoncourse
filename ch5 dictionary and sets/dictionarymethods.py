dict={
    "fast":"In a quick manner",
    "Kiran":"Good Coder",
    "marks":[2,4,5,7],
    "dict2":{
        'Kiran':'A Student',
        'College':'source of knowledge'
    }

}
print (dict.keys())
#type of dictionary
print (type(dict.keys()))
#changing type into list
print (list(dict.keys()))
#printing values
print (dict.values())
#print (keys and values) for all content of the dictionary
print (dict.items())
#updating method
updatedict={
    "Sagar":"Fat Boy",
    "Avinash": "Best Friend", 
    'Kiran':'Friend of Avinash' #it update the given value also
}
dict.update(updatedict)
print (dict)
#get method
print (dict.get("Kiran"))
#difference bitween get and direct method
print (dict.get("rohan")) #prints none when element not found in dictionary
print (dict["rohan"])     #throws erroe when element not found in dictionary