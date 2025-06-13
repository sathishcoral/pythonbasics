
import os
from os import path
import datetime
import time

def main():
    #print(os.name)

    print(path.isfile("testdata.txt"))
    print(path.isdir("testdata.txt"))
    print(path.exists("testdata.txt"))

    print("printing full path", path.realpath("testdata.txt"))
    filepath = path.split(path.realpath("testdata.txt"))
    print("Path alone is = ", filepath[0])
    print("File name is = ", filepath[1])

    print(time.ctime(path.getmtime("testdata.txt")))
    print(datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("testdata.txt")))

    myfile = open("testdata.txt", "r")
    content = myfile.read()
    print(content)

if __name__ == "__main__":
    main()