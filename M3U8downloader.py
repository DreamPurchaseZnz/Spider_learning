"""
Up to now, work well
"""

# -*- coding: utf-8 -*-
import argparse
import math
import os
import random
import urllib
import urllib.error
import urllib.parse
import urllib.request

def print_and_exit(message):
    print(message)
    exit()

def print_log(message):
    import datetime as dt
    print('[%s] %s' % (dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), message))

def get_m3u8(uri):
    import m3u8
    m3u8_obj = None
    urls = []
    if os.path.exists(murl) and os.path.isfile(murl):
        m3u8_obj = m3u8.load(os.path.realpath(murl))
    else:
        try:
            m3u8_obj = m3u8.load(murl)
        except (urllib.error.URLError, ValueError):
            print_and_exit('Invalid M3U8 URL.')
        except Exception:
            print_and_exit('Unexpected Error.')
    for segment in m3u8_obj.segments:
        urls.append(segment.absolute_uri)
    return urls

murl = 'http://video2.fxsdp.com:8091/81820180501/EDRG-007/650kb/hls/index.m3u8'
savp = './'
m3u8_content = get_m3u8(murl)
base_filename = ''.join([random.choice('abcdefghijklmnopqrstuvwxyz0123456789') for i in range(12)])

if os.path.exists(savp) and os.path.isdir(savp):
    savp = os.path.realpath(savp)
else:
    print_and_exit('Invalid saving path.')

def retrieve_file(i):
    url = m3u8_content[i]
    filename = '%s_%s.%s' % (base_filename, \
        str(i + 1).rjust(math.ceil(math.log10(len(m3u8_content))), '0'), \
        url.split('.')[-1])
    try:
        urllib.request.urlretrieve(url, os.path.join(savp, filename))
    except (urllib.error.URLError, ValueError):
        print_and_exit('An invalid media url given.')
    except Exception:
        print_and_exit('Unexpected Error.')
    print_log('File %d of %d downloaded.' % (i + 1, len(m3u8_content)))

print_log('Downloaded files\' names will start with "%s".' % base_filename)
for index, m3u8_url in enumerate(m3u8_content):
    try:
        retrieve_file(index)
    except (urllib.error.URLError, ValueError):
        print_and_exit('An invalid media url given.')
    except KeyboardInterrupt:
        print_and_exit('Program Terminated. Some files are downloaded, and their names start with "%s".' \
            % base_filename)
    except Exception:
        print_and_exit('Unexpected Error.')
print_log('All files downloaded. Their names start with ' + \
    '"%s". You can use "video_combiner.py" to combine them.' % base_filename)
