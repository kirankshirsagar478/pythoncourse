comment=input("Enter the comment:")
spam=False
if ("make a lot money" in comment):
    spam=True
elif ("subscribe this" in comment):
    spam=True
elif ("Buy now" in comment):
    spam=True
else:
    print("Not Spam")

if spam==True:
    print("This is Spam")
