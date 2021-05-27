#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Date        : Tue Jan 26 21:20:26 CET 2021
Autor       : Leonid Burmistrov
Description : Simple reminder-training example.
'''

from optparse import OptionParser

def main_importas():
    print("import pkgttest.module01 as m01")
    print("import pkgttest.module02_class as m02")
    import pkgttest.module01 as m01
    import pkgttest.module02_class as m02
    print("m01.main(./pkgttest/ect/config.json)-->")
    m01.main("./pkgttest/ect/config.json")
    print("m02.main()-->")
    m02.main()

def main_fromimport():
    print("from pkgttest import module01")
    print("from pkgttest import module02_class")
    from pkgttest import module01
    from pkgttest import module02_class
    print("module01.main(./pkgttest/ect/config.json)-->")
    module01.main("./pkgttest/ect/config.json")
    print("module02_class.main()-->")
    module02_class.main()

def main_fromimportas():
    print("from pkgttest import module01 as m01")
    print("from pkgttest import module02_class as m02")
    from pkgttest import module01 as m01
    from pkgttest import module02_class as m02
    print("m01.main(./pkgttest/ect/config.json)-->")
    m01.main("./pkgttest/ect/config.json")
    print("m02.main()-->")
    m02.main()
    
parser = OptionParser()
parser.add_option('-i', '--importas',
                  dest='importas', type="int",default=0,
                  help="try : import ... as ...")
parser.add_option('-f', '--fromimport',
                  dest='fromimport', type="int",default=0,
                  help="try : from ... import ...")
parser.add_option('-a', '--fromimportas',
                  dest='fromimportas', type="int",default=0,
                  help="try : from ... import ... as ...")

(options, args) = parser.parse_args()
    
if __name__ == "__main__":
    if options.importas == 1:
        main_importas()
    elif options.fromimport == 1:
        main_fromimport()
    elif options.fromimportas == 1:
        main_fromimportas()
    else :
        parser.print_help()
        print(options)
