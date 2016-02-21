@echo off

SET BASE_DIR=%~dp0
pushd %BASE_DIR%

SET DOTCOVERBIN=D:\Program Files (x86)\JetBrains\dotCover\v2.7\Bin
SET MSTESTBIN=D:\Program Files (x86)\Microsoft Visual Studio 9.0\Common7\IDE
SET PROJPATH=D:\work\hff_workspace\CCMS\Code\Project\Cmbccd.Common.Test\bin
SET PATH=%DOTCOVERBIN%;%MSTESTBIN%;%PATH%

if exist "%WORKSPACE%\TestResults" ( rmdir /Q /S "%WORKSPACE%\TestResults" )
if exist "%WORKSPACE%\coverage_report" ( rmdir /Q /S "%WORKSPACE%\coverage_report" )
if exist "%PROJPATH%\coverage_report.html" ( del /Q /F "%PROJPATH%\coverage_report.html" )

dotCover.exe analyse /TargetExecutable="%MSTESTBIN%\MSTest.exe" /TargetArguments="/testcontainer:%PROJPATH%\Release\Cmbccd.Common.Test.dll" ^
  /TargetWorkingDir="%PROJPATH%" /Filters=+:module=*;class=*;function=*;-:module=*Common.Test* /ReportType=HTML /Output="%PROJPATH%\coverage_report.html"

popd