import os
def renameall(filepath):
    index=0
    file=os.listdir(filepath)
    # print(file)
    for index,filename in enumerate(file,start=1):
        if file.endswith(".png"):
         os.rename(f"{filepath}\{filename}",f"{filepath}\jay_swaminaryan{index}.jpg")
filepath=input("Enter file path  Carefully! ")
renameall(filepath)
