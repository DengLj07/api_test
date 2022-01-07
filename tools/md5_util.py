# -*- coding: utf-8 -*-
"""

"""
import hashlib

def get_md5(pws):
    md5 = hashlib.md5()
    md5.update(pws.encode('utf-8'))
    return md5.hexdigest()




