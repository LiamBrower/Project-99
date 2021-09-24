import os
import shutil

source = input("")
destination = input('')

source = source + ''
destination = destination + 'Trash'

list_of_files = os.listdir(source)
for file in list_of_files:
    shutil.copy((source+file), destination)
