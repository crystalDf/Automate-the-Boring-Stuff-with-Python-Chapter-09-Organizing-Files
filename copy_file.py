import shutil
import os

print(shutil.copy(os.path.join(os.getcwd(), 'test/c.txt'), os.getcwd()))
print(shutil.copy(os.path.join(os.getcwd(), 'a.txt'),
                  os.path.join(os.getcwd(), 'c.txt')))

print(shutil.copytree(os.path.join(os.getcwd(), 'test'),
                      os.path.join(os.getcwd(), 'test/inner_test2')))

print(shutil.move(os.path.join(os.getcwd(), 'a.txt'),
                  os.path.join(os.getcwd(), 'test')))

print(shutil.move(os.path.join(os.getcwd(), 'b.txt'),
                  os.path.join(os.getcwd(), 'test/bb.txt')))
