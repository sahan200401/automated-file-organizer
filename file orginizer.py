import os
'''
folder_path = input("enter the folder path.. ")

if os.path.exists(folder_path) and os.path.isdir(folder_path):
    print("folder found...")

    items = os.listdir(folder_path)
    print("printing the item in that folder...")

    for item in items:
        full_path = os.path.join(folder_path, item)

        if os.path.isfile(full_path):
            print(item)

        elif os.path.isdir(full_path):
            print("item is folder")

else:
    print("folder not found!  ")


def finding_extension(item):
    os.path.splitext(item)
'''

def file_finding():
    folder_path = input("enter the folder path..")

    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        print("folder found...")

        items = os.listdir(folder_path)
        print("printing the item in that folder..")

        files =[]
        for item in items:
            full_path = os.path.join(folder_path,item)

            if os.path.isfile(full_path):
                files.append(item)

            elif os.path.isdir(full_path):
                print()
        return files
    else:
        print("file not found! ")
        return []

def finding_extension(files):
    extension_list = []
    for item in files:
        file_name,extension = os.path.splitext(item)
        #print(f"{file_name}  ---->  {extension}")
        extension_list.append(extension)

    return list(set(extension_list))



x = file_finding()
print(finding_extension(x))