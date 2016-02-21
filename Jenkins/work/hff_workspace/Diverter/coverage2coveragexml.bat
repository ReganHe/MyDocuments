echo "transfer target coverage to results.coveragexml"
@echo off

SET BASE_DIR=%~dp0
PUSHD %BASE_DIR%

SET COVERAGEHOME=D:\Program Files (x86)\Microsoft Visual Studio 12.0\Team Tools\Dynamic Code Coverage Tools
SET PATH=%COVERAGEHOME%;%PATH%

CodeCoverage analyze /include_skipped_functions /include_skipped_modules /output:D:\work\jenkins\workspace\Diverter\TestResult\testResult.coveragexml D:\work\jenkins\workspace\Diverter\TestResult\testResult.coverage

POPD