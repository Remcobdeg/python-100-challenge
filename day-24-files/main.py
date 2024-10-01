## file reading
file = open("my_text.txt")
contents = file.read()
print(contents)
file.close() #to clean it from memory

with open("my_text.txt") as file:
    contents = file.read()
    print(contents)
#no need to manually close it

## file writing
with open("my_text.txt", mode="w") as file:
    file.write("New text")
    #mode="w" allows (over-)writing; default mode="r" only allows reading
    #creates a new file if it doesn't already exist

with open("my_text.txt", mode="a") as file:
    #mode="a" appends content
    file.write("\nNew text")


## reading exercise:
with open("/Users/b8058356/Desktop/print/test.txt") as file:
    content = file.read()
print(content)

## reading exercise 2 (relative path):
with open("../../../../../../../../Desktop/print/test.txt") as file:
    content = file.read()
print(content)
