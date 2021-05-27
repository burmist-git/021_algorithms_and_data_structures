#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Date        : Tue Jan 26 21:20:26 CET 2021
Autor       : Leonid Burmistrov
Description : Simple reminder-training example.
'''

import os
import sys
#
import algDS

def main():
    os.system('echo "\n 1) Info : --> test of the module01"')
    print(sys.modules['serial_tets'])
    print(sys.modules['serial_tets'].__file__)
    algDS.main()    

if __name__ == "__main__":
    main()
