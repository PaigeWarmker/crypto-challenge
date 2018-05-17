#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import base64

args = sys.argv[1:]
if len(args) < 1:
    print("Provide hex string(s) to convert")
    sys.exit (1)

for s in args:
    b = bytes.fromhex(s)
    print(base64.b64encode(b).decode('utf-8'))
