import os
from shutil import copyfile

fileList = list(range(1, 101))

for item in fileList:
    copyfile('/home/cworrell/projects/bird-brain/blank.jpg', '/home/cworrell/projects/bird-brain/img/bird-' + str(item) + '.jpg')