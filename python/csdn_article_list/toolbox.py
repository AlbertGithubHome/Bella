#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2019-7-28 10:40:47
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : 工具集合，将各种工具放在一起，方便调用

import sys
import random
sys.path.append("..")

from tools.simulate.browserproxies import get_proxies
from tools.simulate.browseragents import *


proxies_list = get_proxies()
def get_random_proxy():
    return random.choice(proxies_list)

