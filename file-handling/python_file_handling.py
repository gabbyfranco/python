# DONE: declare a simple variable called file and assign the open function to it to gain access to a file.
file = open('/test.txt', mode = 'r')

data = file.readline()

print(data)

file.close()