#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import time

L = []

for root, dir, files in os.walk("."):
    for file in files:
        full_path = os.path.join(root, file)
        mtime = os.stat(full_path).st_mtime
        file_modify_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(mtime))
        info = "{0}:{1} 修改时间是: {2}".format(file_modify_time, full_path, file_modify_time)
        L.append(info);

L.sort();
for x in L:
    print(x)