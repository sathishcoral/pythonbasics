
import os
from os import path
import shutil
import zipfile
from zipfile import ZipFile
import glob

def main():
    if path.exists("testdata.txt.old"):
        #print("File present")
        
        # get the path to the file in the current directory
        srcfile = path.realpath("testdata.txt.old ")

        # let's make a backup copy by appending "bak" to the name
        #newfile = srcfile + ".old"
        #shutil.copy(srcfile,newfile)
        
        # rename the original file
        #os.rename("testdata.txt", "renamedfile.txt")

        # now put things into a ZIP archive
        pathonly, file = path.split(srcfile) 
        shutil.make_archive("newarch","zip", pathonly)

        # more fine-grained control over ZIP files
        #newzip = ZipFile("twofilezip.zip","w")
        with ZipFile("twofilezip.zip", "w") as newzip:
            for file in glob.glob("*.txt*"):
                newzip.write(file)


if __name__ == "__main__":
    main()