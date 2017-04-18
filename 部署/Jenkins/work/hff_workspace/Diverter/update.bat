@echo off

set BASE_DIR=%~dp0
pushd %BASE_DIR%

set PATH=%PATH%;C:\PROGRA~2\Hansky\Firefly\Client\bin\java
:: 更新本地配置文件
hff bringover %1

popd
