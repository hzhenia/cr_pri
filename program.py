#!/usr/bin/env python
from  features import  features_extract
datafile = 'data.txt'
def main():
    f = open(datafile,'r')
    features_speed = {}
    features_supplier = {}
    for line in f:
        res = features_extract.get_feature(line)
        print line.rstrip()
        print res
        print "----------------------"
if __name__ == "__main__":
    main()
