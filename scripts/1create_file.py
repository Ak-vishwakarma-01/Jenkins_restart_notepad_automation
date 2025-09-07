import  os


folder_path = r"C:\Users\ak_vishwakarma_0\Desktop\jenkins Automation\automation"
os.makedirs(folder_path,exist_ok=True)


file_path = os.path.join(folder_path,"first_file.txt")
with open(file_path,"w") as file:
    file.write("This is my first automated file!")

print(f"File created at: {file_path}")