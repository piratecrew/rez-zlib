# -*- coding: utf-8 -*-

name = 'zlib'

version = '1.2.11'

authors = ['fredrik.brannbacka']

def commands():
    env.LD_LIBRARY_PATH.prepend("{root}/lib")
    if building:
        env.CMAKE_MODULE_PATH.append("{root}/cmake")