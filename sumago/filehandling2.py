f=open("file.txt", 'a+')
print("Enter Content('press enter to exit'):")
data=""
while data!='exit':
    f.write(data+"\n")
    data=input()
f.close()
print("File Written successfully...")