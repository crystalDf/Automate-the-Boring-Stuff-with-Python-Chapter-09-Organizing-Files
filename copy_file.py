import shutil
import os
import send2trash

# print(shutil.copy(os.path.join(os.getcwd(), 'test/c.txt'), os.getcwd()))
# print(shutil.copy(os.path.join(os.getcwd(), 'a.txt'),
#                   os.path.join(os.getcwd(), 'c.txt')))
#
# print(shutil.copytree(os.path.join(os.getcwd(), 'test'),
#                       os.path.join(os.getcwd(), 'test/inner_test2')))
#
# print(shutil.move(os.path.join(os.getcwd(), 'a.txt'),
#                   os.path.join(os.getcwd(), 'test')))
#
# print(shutil.move(os.path.join(os.getcwd(), 'b.txt'),
#                   os.path.join(os.getcwd(), 'test/bb.txt')))

# print(os.unlink(os.path.join(os.getcwd(), 'test/bb.txt')))
# print(os.rmdir(os.path.join(os.getcwd(), 'test/inner_test')))
# print(shutil.rmtree(os.path.join(os.getcwd(), 'test/inner_test')))

# baconFile = open('bacon.txt', 'a')
# print(baconFile.write('Bacon is not a vegetable.'))
# baconFile.close()
# send2trash.send2trash('bacon.txt')

for folderName, subfolders, filenames in os.walk(os.getcwd()):
    print('The current folder is ' + folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ": " + subfolder)

    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': ' + filename)

    print()

