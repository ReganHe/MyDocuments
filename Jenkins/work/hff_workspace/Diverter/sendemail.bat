@echo off
set base_dir=%~dp0
pushd %base_dir%

set PATH=%PATH%;D:\Python27
python.exe "D:\\work\\hff_workspace\\Vortex\\sendemail4ccms.py" %1 %2 %3

popd
