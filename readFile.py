# import docx

# #declare a function to read word file

# def readWordFile(file):
#     doc = docx.Document(file)

#     text = []

#     for i in doc.paragraphs:
#         text.append(i.text)
    
#     return '\n'.join(text)

# print(readWordFile('file.txt'))

# opening the text file
with open('file.txt','r') as file:
    # reading each line
    for line in file:
        # reading each word
        for word in line.split():
            # displaying the words
            print(word)