filename = input("Enter File Name to open: ")

filepointer = open(filename, 'r')
lines = list(filepointer)
print(lines)

line_no = int(input("Which line to delete: "))
del lines[line_no]

filepointer.close()

filepointer = open(filename, 'w')
for l in lines:
    filepointer.write(l)
filepointer.close()
