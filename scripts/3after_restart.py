import os

folder_path = r"C:\Users\ak_vishwakarma_0\Desktop\jenkins Automation\automation"
file_path = os.path.join(folder_path, "after_restart_file.txt")

with open(file_path, "w") as file:
    file.write("This file is created after computer restart!")

print("After restart script executed.")
