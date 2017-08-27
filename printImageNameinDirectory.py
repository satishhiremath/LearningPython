import os, glob

os.chdir("C:/Users/User/PycharmProjects/practice")

for file in glob.glob("*.jpg"):
    print(file)