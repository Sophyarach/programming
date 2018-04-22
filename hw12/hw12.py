import os
import re

def files_wo_digits():
    n=0
    file_list=os.listdir()
    print('Файлы без цифр в названии:')
    for file in file_list:
        if os.path.isfile(file):
            if not re.search(r'[0-9]',file):
                n+=1
                print(file)
    print('Файлов без цифр в названии : ', n, '\n')

def all_files():
    print('Все файлы:')
    file_list=os.listdir()
    for file in file_list:
        print(file)

files_wo_digits()
all_files()
