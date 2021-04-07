import os
from pathlib import Path

user_directory = input("Input your desired directory.\n")
print("Checking directory... (User Input = " + user_directory + ")")
if (Path(user_directory).exists() == True):
    print("Path exists, redirecting...")
    os.chdir(user_directory)
else:
    print("Path is invalid, script exiting.")
    sys.exit(0)

DeletedFileCount = 0
RenamedFileCount = 0
for f in os.listdir():
    file_name, file_ext = os.path.splitext(f)
    new_path = os.path.join(user_directory, f)

    if int(file_name)%2 == 0:
        DeletedFileCount+= 1
        print("Deleting " + new_path)
        os.remove(new_path);
        print("Deleted " + str(DeletedFileCount) + " files.")
    else:
        renamed_file_path = os.path.join(user_directory, str(RenamedFileCount) + file_ext)
        os.rename(new_path, renamed_file_path)
        print("Renamed:\n" + new_path + "\nto:\n" + renamed_file_path)
        RenamedFileCount += 1
