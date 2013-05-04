import os

dir = os.getcwd()

print dir

os.chdir('/opt')

print os.getcwd()

os.chdir(dir)

print os.getcwd()

os.system('ls')