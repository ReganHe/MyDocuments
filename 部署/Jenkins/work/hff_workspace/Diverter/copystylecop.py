
import os
import os.path
from shutil import copy

dest_dir = r'D:\work\jenkins\workspace\Diverter\StyleCopResult\Business.xml'
file_path = r'D:\work\hff_workspace\Diverter\Code\Project\Diverter\Diverter.Business\obj\Release\StyleCopViolations.xml '
copy(file_path, dest_dir)

dest_dir = r'D:\work\jenkins\workspace\Diverter\StyleCopResult\Common.xml'
file_path = r'D:\work\hff_workspace\Diverter\Code\Project\Diverter\Diverter.Common\obj\Release\StyleCopViolations.xml'
copy(file_path, dest_dir)

dest_dir = r'D:\work\jenkins\workspace\Diverter\StyleCopResult\ExternalService.xml'
file_path = r'D:\work\hff_workspace\Diverter\Code\Project\Diverter\Diverter.ExternalService\obj\Release\StyleCopViolations.xml'
copy(file_path, dest_dir)

