import os
import shutil
s = r"C:\Users\user653\Desktop\New folder\file.txt"
d = r"C:\Users\user653\Documents\doc"
files = os.listdir(s)
shutil.copytree(s, d)
print("copied")

