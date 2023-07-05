f=open("file.txt", 'a+')
print("Enter Content('press enter to exit'):")

while True:
    content = input()
    if content == "exit":
        print("Exiting the file.......")
        break
    f.write(content + "\n")
print("Content written to the file!!!!!!!")

