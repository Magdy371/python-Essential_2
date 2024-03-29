# file descriptor: 1
# a token generated by the OS that allows the program to do more operations on the file
#to open the file in the same folder
file = open("spider.txt")

# to read the first line in the file
print(file.readline())

# to read the second line in the file
print(file.readline()) #  AND SO ON

# SO WE CAN USE A LOOP TO READ ALL THE LINES IN THE FILE
# for line in file:
#     print(line)
#or we can use read() method to read the whole file
# eavery time we call the read or readline method the file pointer moves to the next line
#so the read method will read the file from the current position of the file pointer wj==hich is line 3
print(file.read())

# to close the file
# its important to close the file after we finish working with it
# beacause the OS has a limit on the number of files that can be open at the same time
file.close()