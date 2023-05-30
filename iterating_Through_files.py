with open("spider.txt") as file:
    for line in file:
        print(line.upper())

# the second one will leave white space between the lines
# to remove the white space we use strip() method
with open("spider.txt") as file:
    for line in file:
        print(line.strip().upper())

# we can traite the file as a list
# \n is a new line character | \t is a tab character
file = open("spider.txt")
lines = file.readlines()
file.close()
lines.sort()
print(lines)

