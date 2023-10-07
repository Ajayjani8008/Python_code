import os
def renameall(filepath):
    index=0
    file=os.listdir(filepath)
    # print(file)
    for index,filename in enumerate(file,start=1):
        os.rename(f"{filepath}\{filename}",f"{filepath}\Jay_swaminrayan{index}.jpg")


filepath=input("Enter file path  Carefully! ")
renameall(filepath)

   