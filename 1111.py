import os
import shutil
#
# os.chdir('./..')  # change directory (./..) one level up
# print(os.getcwd())  # где находится поточный файл
#
# os.chdir('D:\AQA_Hillel\\venv')  # change directory with full absolute path
# print(os.getcwd())
#
# print(os.listdir('./..'))  # list of internal directories and/or files
#
# print(os.getcwd())
#
# for f in os.listdir('./..'):  # search files by specified criteria in a directory
#     if f.endswith('1.py'):
#         print(f)
#
# print([k for k in os.listdir(r'D:\34qa') if k.startswith('Ho')])  # search by specified criteria in one line
#
# os.chdir('./..')
# print(os.getcwd())
# print(os.listdir())  # a list of current files and folders
#
# os.mkdir('test_folder')  # create a new folder
# print(os.listdir())
#
# os.rmdir('test_folder')  # remove a directory (the command won't work if your folder is not empty)
# print(os.listdir())
#
# """
# os.makedirs('test/1/2')  # creating multiple folders (create new folder in a new folder, in a new folder)
# print(os.listdir())
#
# os.remove('test.txt')  # remove a file
#
# fl_to_del = (r'D:\AQA_Hillel\test')  # recursively remove a directory tree
# shutil.rmtree(fl_to_del)
# """
#
# print(os.environ)  # "list" of environment variables
#
# print([q for q in os.environ])  # list of keys of our environment variables
# print(os.environ.get('key'))  # we can find the value of a variable if we know the key
#
# os.environ['123'] = 'QWE'  # we can add a new pair of env.variable ['key'] = 'value'
# print(os.environ)  # show the "list" of env.variables
# print(os.environ.get('123'))  # find the value by knowing the key
#
# print(os.environ.get('123'))
#
# os.system('set ENV_VAR_2=env_test_123')  # можно запускать какие-то команды системы
# print(os.system('set'))
#
# os.system(r'C:\Users\Pavilion\Desktop\script.sh.sh')  # можно запускать баш-скрипты, например
# os.walk('')
# for dp, dn, fn in os.walk('.'):
#     print(dp, dn, fn, sep='\n', end='\n+-+-+-+-+-+-+-+-+-+-+-+-+\n')
#
# print(os.path.join(os.path.abspath(''), 'HomeWork_2.py'))  # можно получить полный путь к ва
# with open('D:\departments.json', 'r') as f:
#     print(f.read())
#
# with open('test.txt', 'w') as t:  # write in a file
#     row = 'new line'
#     t.write(row)
#
# with open('test.txt', 'r') as t:  #read from a file
#     print(t.read())
#
# s = os.path.getsize('test.txt')  # get file size
# print(s)