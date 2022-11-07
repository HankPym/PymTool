

from os import walk

# folder path
dir_path = r'C:\\Users\\lesfi\\OneDrive\\'

# list to store files name
myFiles = []
for root,dirs,files in walk(dir_path):
	myFiles.extend(files)
    
File_object = open(r"C:\\Test\\filelist.txt", "w")
File_object.writelines(myFiles)
File_object.close