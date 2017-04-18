@echo off

set BASE_DIR=%~dp0
pushd %BASE_DIR%

SET PATH=%PATH%;C:\PROGRA~2\Hansky\Firefly\Client\bin\java
hff info %1

popd