import os

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
