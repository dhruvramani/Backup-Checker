import os
import sys

dirF = list()
def checkDir(originalDir, backupDir):
    lsOut = os.popen('ls -a {}'.format(originalDir)).read().split()
    lsBackOut = os.popen('ls -a {}'.format(backupDir)).read().split()
    print('Scanning Through {}'.format(originalDir))
    
    for i in lsOut[2:]:
        if os.path.isdir('{}/{}'.format(originalDir,i)):
            if i in lsBackOut:
                checkDir('{}/{}'.format(originalDir, i), '{}/{}'.format(backupDir, i)) 
            else :
                dirF.append('\033[1m\033[92m==>\033[0m Directory \033[4m{}/{}\033[0m Needs to be Backed-up\033[0m'.format(originalDir,i))
        elif os.path.isfile('{}/{}'.format(originalDir,i)):
            if i not in lsBackOut:
                dirF.append('\033[1m\033[94m==>\033[0m File \033[4m{}/{}\033[0m Needs to be Backed-up\033[0m'.format(originalDir,i))

def main():
    
    if len(sys.argv) == 1: 
        dir = '{}/{}'.format(os.getcwd(), input('Enter Relative Directory : '))
        backupDir = '/Volumes/{}'.format(input('Enter Backup_Disk/Directory_Name : '))
    else :
        dir = '{}/{}'.format(os.getcwd(),sys.argv[1])
        backupDir = '/Volumes/{}'.format(sys.argv[2])

    checkDir(dir, backupDir)
    print('\n' + '\n'.join(dirF))

if __name__ == '__main__':
    main()