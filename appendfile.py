filename = input("Enter a File Name: ")
filepointer = open(filename + ".txt", 'a')

line = input("Enter Text, type !q to quit: ")

while line != "!q":
    filepointer.write(line+"\n")
    line = input("Enter Text, type !q to quit: ")
filepointer.close()