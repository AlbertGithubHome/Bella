#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import bcrypt

passwd = b'123456nx'

start = time.time()
salt = bcrypt.gensalt()
pwsd = bcrypt.hashpw(passwd, salt)

cost = time.time() - start
print("[salt]", salt)
print("[pwsd]", pwsd)
print("[cost]", cost)