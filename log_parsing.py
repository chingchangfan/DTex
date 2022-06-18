#1/usr/bin/env python


import re


sample_log = """
111.222.333.123 HOME - [01/Feb/1998:01:08:39 -0800] "GET /bannerad/ad.htm HTTP/1.0" 200 198 "http://www.referrer.com/bannerad/ba_intro.htm" "Mozilla/4.01 (Macintosh; I; PPC)"
111.222.333.123 HOME - [01/Feb/1998:01:08:46 -0800] "GET /bannerad/ad.htm HTTP/1.0" 200 28083 "http://www.referrer.com/bannerad/ba_intro.htm" "Mozilla/4.01 (Macintosh; I; PPC)"
111.222.333.123 AWAY - [01/Feb/1998:01:08:53 -0800] "GET /bannerad/ad7.gif HTTP/1.0" 200 9332 "http://www.referrer.com/bannerad/ba_ad.htm" "Mozilla/4.01 (Macintosh; I; PPC)"
111.222.333.123 AWAY - [01/Feb/1998:01:09:14 -0800] "GET /bannerad/click.htm HTTP/1.0" 200 207 "http://www.referrer.com/bannerad/menu.htm" "Mozilla/4.01 (Macintosh; I; PPC)"
"""

out_file = 'output.csv'

with open(out_file, 'w+') as f:
    for line in sample_log.split('\n'):
        if re.search(r'\d+\.\d+\.\d+\.\d+', line):
            match = line.split('"')
            http_method = match[1].split()[0]
            resp_code, bytes_trans = match[2].split()
            url = match[3]
            user_agent = match[5]
            f.write(http_method + ', ' + bytes_trans + ', ' + resp_code + ', ' + user_agent + ', ' + url + '\n')
