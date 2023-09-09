import os
from pathlib import Path

def cls():
    '''Fn to clear the python console'''
    os.system('cls')

src_path = 'D:/Coding/GIT/udemy/Python 100 days of coding/python_practices/python file renamer/'
cleaned_lines = []

dir = os.listdir( src_path )
for file in range(len(dir)):
    file_without_ext = dir[file]
    dir[file] = file_without_ext
print(dir)

cls()

filename = "rename.txt"
path = f"{src_path}rename.txt"
check_file = os.path.isfile(path)
print(check_file)
if check_file:
    with open(f'{src_path}rename.txt') as f:
        lines = f.readlines()
        for line in lines[1:]:
            info = line.split()
            # print(info)
            product_id = info[0]
            product_name = info[1]
            cleaned_lines.append([product_id, product_name])
    
    print(f"Cleaned lines are {cleaned_lines}")

    print(f"The file {filename} was found.")
    for product in range(len(cleaned_lines)):
        tif_id = cleaned_lines[product][0]
        tif_name = cleaned_lines[product][1]
        for file in dir:
            if tif_name == file.rsplit( ".", 1 )[ 0 ]:
                # print(f"File {file} was renamed to {tif_id}.tif")
                os.rename(f"{src_path}{file}",f"{src_path}{tif_id}.tif")
            else:
                print(f"No matching tif id for {file}")
else:
    print(f"The file {filename} was not found.")