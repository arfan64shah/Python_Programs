file = open('file.txt', 'r')

content = file.read()

print(content)

file.close()

file1 = open('file1.txt', 'w')
file1.write("My name is Arfan Shah and I am fresh graduate aimimg to pursue Data Science as it is the \
            my favorite field and I am really comfortable working with data.")
file1.close()

file1 = open('file1.txt', 'a')
file1.write("\nI want to be the world's richest businessman and I am working hard for it.")