import os
import re

def count_cyr_names(path):
    n=0
    for root,dirs,files in os.walk(path):
        for d in dirs:
            if re.match("^[а-яА-ЯёЁ]*$", d):
                n+=1
    return n

print ("Папок с полностью кириллическим названием", count_cyr_names("."))
