# Label the program written in problem 4 with comments.
import os

# Specify the directory path
directory = '.'  # current directory

# Print the contents of the directory
contents = os.listdir(directory)

for item in contents:
    print(item)