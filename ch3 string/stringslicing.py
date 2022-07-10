name="kiran"
print (name[0])
print (name[1])
print (name[2])
print (name[0:3])
print (name[1:4])
print (name[0:5]) #is equal to:
print (name[:5]) #blank is equal to begining

print (name[1:]) #is same as name[1:5] , here blank space is equal to end

#Negative indexes
print (name[-5:-1])
# print (name[-1:-5])  wrong not working

#string sclising with skip value
print (name[0::2]) #it will skip value after two characters
print (name[1:5:3]) #it will skip value after three characters

