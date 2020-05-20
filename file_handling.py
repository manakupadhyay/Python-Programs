# FILE HANDLING IN PYTHON...

# open() syntax : open('filename', 'mode') --- it returns a file object...

# file = open('text.txt', 'r')                                                  ''' reading from a file '''
# variable = 50
# file_contents = file.read(variable)
# while len(file_contents) > 0:
#     print(file_contents, end='')
#     file_contents = file.read(variable)

# file = open("text_copy.txt", 'w')                                             ''' writing to a file '''
# file.write('I am a copy of text file that i downloaded from github\n')
# file.write('I am a copy of text file.')
# file.close()

# file = open('text.txt', 'r')
# print(file.readline(), end='')
# file.seek(3)                                                    # it brings the file pointer to the specified position...
# print(file.tell())                                              # it tells the position of file pointer...


'''
if we are using with statement to perform file operations then we don't need to explicitly close the file. This is like
try with resources in Java.
'''

with open('text.txt', 'r') as rf:
    ''' code to copy the contents of one file and insert it to another...'''
    with open('text_copy.txt', 'w') as wf:
        for each_line in rf:
            wf.write(each_line)

'''
    we can also copy the contents of an image... for that we just have to change the mode from 'r' to 'rb' for bytes(unicode to bytes)
'''



