# we can do some basic operation on file from FileBasic_1.py in one statement
#we use with statement to open the file and close it automatically
with open("spider.txt") as file:
    print(file.read())