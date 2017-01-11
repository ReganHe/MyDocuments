# -*- coding: gb2312 -*- 
from __future__ import print_function
import os, sys
import zipfile

def zip_dir(dirname,zipfilename):
    filelist = []
    if not os.path.isdir(dirname):
        print(" @@@@@@@@@@ invalid parameter: "+dirname)
        return
    for root, dirs, files in os.walk(dirname):
        for name in files:
            filelist.append(os.path.join(root, name))
    zf = zipfile.ZipFile(zipfilename, "w", zipfile.zlib.DEFLATED)
    for tar in filelist:
        arcname = tar[len(dirname):]
        zf.write(tar,arcname)
    zf.close()

if __name__ == "__main__":
    if len(sys.argv) != 3 :
        print("命令行缺少参数,正确调用格式：zip.py dirname zipfilename")
        exit(1)
    
    dirname = sys.argv[1]
    zipfilename = sys.argv[2]
    
    zip_dir(dirname, zipfilename)
    
    exit(0)