


file = open(r"C:\Users\Sandeep\Desktop\data\cr-copy.txt", "a")
content = "\nThis content will be written to file"
file.write(content)
file.close()

with open(r"C:\Users\Sandeep\Desktop\data\cr-copy.txt", "a") as file :
    content = "\nThis content will be written to file"
    file.write(content)
