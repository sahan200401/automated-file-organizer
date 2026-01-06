import shutil
import  os

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
        return files,folder_path
    else:
        print("file not found! ")
        return []


def finding_extension(files,folder_path):
    extension_list = []
    for item in files:
        file_name,extension = os.path.splitext(item)
        #print(f"{file_name}  ---->  {extension}")
        extension_list.append(extension)

    return list(set(extension_list))


def find_Category(extension):
    categories = {
        "Images": [".jpg", ".png", ".jpeg"],
        "Documents": [".pdf", ".txt", ".docx"],
        "Videos": [".mp4", ".mkv"],
        "Code": [".py", ".java", ".js"]
    }

    for category,ext_lst in categories.items():
        if extension.lower() in ext_lst:
            return  category

    return "other"


def organize_files(files,folder_path):
    for file in files:
        source_path = os.path.join(folder_path,file)
        _,extension = os.path.splitext(file)
        category = find_Category(extension)

        category_path = os.path.join(folder_path,category)
        if not os.path.exists(category_path):
            os.mkdir(category_path)

        destination_path = os.path.join(category_path, file)
        shutil.move(source_path, destination_path)


files, folder_path = file_finding()
if files:
    print(f"Extensions found: {finding_extension(files, folder_path)}")

    # Print category mapping
    for ext in finding_extension(files, folder_path):
        print(f"{ext} → {find_Category(ext)}")

    # Organize files
    organize_files(files, folder_path)
    print("Files organized successfully!")