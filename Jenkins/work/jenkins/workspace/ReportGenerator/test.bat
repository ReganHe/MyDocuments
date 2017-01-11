SET REPORTHOME=D:\work\jenkins\workspace\Diverter\ReportGenerator
SET PATH=%REPORTHOME%;%PATH%;

ReportGenerator.exe -reports:D:\work\jenkins\workspace\Diverter\TestResult\testResult.coveragexml -targetdir:D:\work\jenkins\workspace\Diverter\Report -reporttypes:Html