import os
import glob

files_list = glob.glob('F:/FrontCourse/session3/*')

suffix_set = set()

for i in files_list:
    suffix = i.split('.')[-1]
    suffix_set.add(suffix)

def create_folder():
    for i in suffix_set:
        if i == 'py':
            continue
        else:
            os.makedirs('F:/FrontCourse/session3/' + i)

def move_file():
    for file in files_list:
        suffix = file.split('.')[-1]
        file_name = file.split('\\')[-1]
        os.rename(file,'F:/FrontCourse/session3/' + suffix +'/'+ file_name)

create_folder()
move_file()