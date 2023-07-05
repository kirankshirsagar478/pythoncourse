f=open("file.txt","a+")
f.write("python class")
lst=['Line1','Line2','Line3']
f.writelines(lst)
print(f.readlines())
f.close()

