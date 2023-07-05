paragraph = "Kiran Kshirsagar is a student. He is studying in IT branch of Amrutvahini College."
word = input("Enter a string to search in the paragraph: ")

if word.lower() in paragraph.lower():
    print("The paragraph contains the string.")
else:
    print("The paragraph does not contain the string.")
