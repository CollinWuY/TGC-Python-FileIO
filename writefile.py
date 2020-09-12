#open file info.txt in write mode
#if file dont exist python will create it
#if file exist python will overwrite it

filepointer = open('info.txt', 'w')
filepointer.write("Chicken Tigh\n")
filepointer.write("Fresh Milk\n")
filepointer.write("Toilet Roll\n")
filepointer.close()