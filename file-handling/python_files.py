# DONE: use a with statement with the open function
with open('newfile.txt', mode='w') as file:
# TODO: add content to the file using the write function.
    file.writelines(["This is a new file created!", "\nThis is another line to be added."])