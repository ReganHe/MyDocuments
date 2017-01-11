
from __future__ import print_function
import zipfile, sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Error Command Paramters, it should like this: unzip.py srcZipfile dstDirectory ")
        exit(1)
    
    srcZipfile = sys.argv[1]
    dstDirectory = sys.argv[2]
    print(" UNZIP ["+ srcZipfile +"] to directory ["+ dstDirectory +"] ....")
    
    try:
        with zipfile.ZipFile(srcZipfile, 'r') as zipread:
            zipread.extractall(dstDirectory)
    except Exception as Err:
        print(" !!!!!!!! UNZIP file failed, Err:" + str(Err))
        exit(1)
    
    print(" !!!!!!!! UNZIP file SUCCESS !!!!!!!! ")
    exit(0)
