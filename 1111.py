import os
import shutil

os.chdir('./..')  # change directory (./..) one level up
print(os.getcwd())  # где находится поточный файл

os.chdir('D:\AQA_Hillel\\venv')  # change directory with full absolute path
print(os.getcwd())

print(os.listdir('./..'))  # list of internal directories and/or files

print(os.getcwd())

for f in os.listdir('./..'):  # search files by specified criteria in a directory
    if f.endswith('1.py'):
        print(f)

print([k for k in os.listdir(r'D:\34qa') if k.startswith('Ho')])  # search by specified criteria in one line

os.chdir('./..')
print(os.getcwd())
print(os.listdir())  # a list of current files and folders

os.mkdir('test_folder')  # create a new folder
print(os.listdir())

os.rmdir('test_folder')  # remove a directory (the command won't work if your folder is not empty)
print(os.listdir())

os.makedirs('test/1/2')  # creating multiple folders (create new folder in a new folder, in a new folder)
print(os.listdir())

os.remove('test.txt')  # remove a file

fl_to_del = (r'D:\AQA_Hillel\test')  # remove a tree of directories
shutil.rmtree(fl_to_del)

