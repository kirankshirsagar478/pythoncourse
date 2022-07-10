letter='''Dear <|NAME|>,
We are glad to inform you that you are invited to our coding project exibition.
Your participation will good for us.
Your Sincerly,
Kiran Kshirsagar
Date:<|DATE|>'''
print (letter)
name=input("Enter Your Name:\n")
date=input("Enter Date:\n")
letter=letter.replace("<|NAME|>",name)
letter=letter.replace("<|DATE|>",date)
print (letter)