```
not work well
```
# -*- coding: utf-8 -*-
import argparse
import os
import platform
import random
import re
import subprocess
import datetime as dt

def print_and_exit(message):
    print(message)
    exit()

def print_log(message):
    print('[%s] %s' % (dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), message))

p = 'x3bykmcmfspj_\d{4}.ts'
pwd = os.getcwd()

# check ffmpeg binary file
ffmpeg_bin = 'ffmpeg.exe' if 'Windows' in platform.system() else 'ffmpeg'
ffmpeg_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'ffmpeg', ffmpeg_bin)
print(ffmpeg_path)
if not os.path.exists(ffmpeg_path):
    print_and_exit('Cannot find ffmpeg.')
ffmpeg_path = os.path.realpath(ffmpeg_path)

# get file list
all_files = [os.path.split(x)[-1] for x in os.listdir(pwd) if os.path.isfile(x)]
regex = re.compile(p)
print('Using pattern: "%s"' % p)
all_files = [x for x in all_files if regex.fullmatch(x) != None]
print('Got files: %s' % ', '.join(all_files))

# generate ffconcat file
ffconcat_filename = ''
output_filename = ''
while ffconcat_filename == '' or os.path.exists(ffconcat_filename) or os.path.exists(output_filename):
    output_filename_prefix = ''.join([random.choice('abcdefghijklmnopqrstuvwxyz0123456789') for i in range(12)])
    ffconcat_filename = output_filename_prefix + '.txt'
    output_filename = output_filename_prefix + '.mp4'
try:
    with open(ffconcat_filename, 'w+') as fp:
        for x in all_files:
            fp.write('file \'%s\'\n' % x)
except Exception as err:
    if os.path.exists(ffconcat_filename):
        os.remove(ffconcat_filename)
    print_and_exit('Got an unexpected error: %s.' % str(err))

# execute ffmpeg
ffmpeg_process = subprocess.Popen([ffmpeg_path, '-f', 'concat', '-i', ffconcat_filename, '-c', 'copy', output_filename], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print('\n\nffmpeg is working, please wait...\n')
ffmpeg_stdout, ffmpeg_stderr = ffmpeg_process.communicate()
ffmpeg_result = ffmpeg_process.returncode

# do some cleaning
if ffmpeg_result != 0:
    if os.path.exists(ffconcat_filename):
        os.remove(ffconcat_filename)
    if os.path.exists(output_filename):
        os.remove(output_filename)
    print('An error occurred during running ffmpeg.')
    print_and_exit((ffmpeg_stdout, ffmpeg_stderr))
else:
    if os.path.exists(ffconcat_filename):
        os.remove(ffconcat_filename)
    print_and_exit('Done. Output file is %s.' % output_filename)
