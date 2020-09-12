#open a file for reading
filename =input("Please Enter File Name: ")

filepointer = open(filename)
for line in filepointer:
    print(line.strip())