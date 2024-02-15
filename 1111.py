import os

os.chdir('./..') # change directory (./..) one level up
print(os.getcwd()) # где находится поточный файл

os.chdir('D:\AQA_Hillel\\venv') # change directory with full absolute path
print(os.getcwd())

print(os.listdir('./..')) # list of internal directories and/or files

print(os.getcwd())

for f in os.listdir('./..'): # search files in a directory
    if f.endswith('1.py'):
        print(f)