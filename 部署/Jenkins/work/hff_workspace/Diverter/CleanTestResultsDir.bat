@echo off

set BASE_DIR=%~dp0
pushd %BASE_DIR%

rmdir /s /q D:\work\hff_workspace\Diverter\TestResults
mkdir D:\work\hff_workspace\Diverter\TestResults

popd
