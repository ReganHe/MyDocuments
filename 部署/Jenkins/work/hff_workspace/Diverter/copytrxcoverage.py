__author__ = ''
import os
trxs = []
covers = []
home = r'D:\work\hff_workspace\Diverter'
os.chdir(home)

workplace = os.path.join(home, 'TestResults')
os.chdir(workplace)
print(os.getcwd())

for root, dirs, files in os.walk(workplace):
    trxs.extend([os.path.join(root, f) for f in files if f.endswith('.trx')])
    covers.extend([os.path.join(root, f) for f in files if f.endswith('.coverage')])
for trx in trxs:
    print(trx)
    os.rename(trx, r'D:\work\jenkins\workspace\Diverter\TestResult\testResult.trx')
os.rename(covers[0], r'D:\work\jenkins\workspace\Diverter\TestResult\testResult.coverage')




