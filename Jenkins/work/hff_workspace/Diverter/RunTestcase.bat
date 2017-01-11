echo "run test case"
@echo off

set BASE_DIR=%~dp0
pushd %BASE_DIR%

SET PATH=%PATH%;D:\Program Files (x86)\Microsoft Visual Studio 12.0\Common7\IDE
SET PATH=%PATH%;D:\Program Files (x86)\Microsoft Visual Studio 12.0\Common7\IDE\CommonExtensions\Microsoft\TestWindow

vstest.console.exe Code\Project\Diverter\Diverter.UnitTests\bin\Release\Diverter.UnitTests.dll /Settings:Local.runsettings /inIsolation /EnableCodeCoverage /logger:trx
popd
