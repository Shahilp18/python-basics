
#! To read files
#? if we don't write "r" BY DEFAULT it is read mode.
with open("/Applications/Career/Python/File/sample.txt", "r") as f:
    # data = f.read()
    data1 = f.readline() #? prints next line 
    data2 = f.readline() #? prints next line 
    print(data1)
    print(data2)
# f.close() #? (It auto-closes the file) with keyword


#! To write files 
# f1 =  open("/Applications/Career/Python/File/sample.txt", "w")
f1 =  open("/Applications/Career/Python/File/sample.txt", "a")

# f1.write("Text overwritten by f1.write...")
f1.write("\nUsed Append...") #? Append

f1.close()

#! To create new file use: x
f3 = open("/Applications/Career/Python/File/sample2.txt", "x")

f3.write("Created new file using x")
f3.close()


#* r+ | a+ | w+ 

#! Delete files
import os

os.remove("/Applications/Career/Python/File/sample2.txt")