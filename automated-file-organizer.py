'''import os

folder_Path = input("Enter folder path: ")

if os.path.exists(folder_Path) and os.path.isdir(folder_Path):
    print("folder found..")

    items = os.listdir(folder_Path)
    print("intem inside the folder :")

    for item in items:
        full_path = os.path.join(folder_Path,item)
        if os.path.isfile(full_path):
            print("item is file :")
        elif os.path.isdir(full_path):
            print("item is folder :")    
        print(item)

else:
    print("folder not found..")     '''


categories = {
        "Images": [".jpg", ".png", ".jpeg"],
        "Documents": [".pdf", ".txt", ".docx"],
        "Videos": [".mp4", ".mkv"],
        "Code": [".py", ".java", ".js"]
    }


for key,item in categories.items():
    print(f"category : {key} ////  extensions : {item}")