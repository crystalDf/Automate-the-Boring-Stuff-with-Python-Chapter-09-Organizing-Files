import zipfile
import os

exampleZip = zipfile.ZipFile(os.path.join(os.getcwd(), 'example.zip'))
print(exampleZip.namelist())
spamInfo = exampleZip.getinfo('spam.txt')
print(spamInfo.file_size)
print(spamInfo.compress_size)
print('Compressed file is %sx smaller!' % (round(spamInfo.file_size /
                                                 spamInfo.compress_size, 2)))

# exampleZip.extractall(os.path.join(os.getcwd(), 'delicious'))
print(exampleZip.extract('spam.txt'))
print(exampleZip.extract('spam.txt', os.path.join(os.getcwd(), 'test')))

exampleZip.close()
