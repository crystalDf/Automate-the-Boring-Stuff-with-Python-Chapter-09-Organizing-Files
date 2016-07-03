import shutil
import os

print(shutil.copy(os.path.join(os.getcwd(), 'Test/c.txt'), os.getcwd()))
print(shutil.copy(os.path.join(os.getcwd(), 'a.txt'),
                  os.path.join(os.getcwd(), 'b.txt')))
