SUPPLIER_DATA  = 'suppliers.txt'
def main():
    res = []
    #build matching
    pattern = ["supplier","port","memtype","cputype","brand" ]
    o= open("regpattern.py","w")
    for p in pattern:
        f = open(p+"s.txt",'r')
        pat_str = ""
        for l in f:
            pat_str =  pat_str  + '|' + l.rstrip()
        pat_str = p.upper() + "PATTERN = '" + pat_str[1:] +"'"
        f.close()
        o.write(pat_str)
        o.write("\n")
    o.close()
    print "Finished"
if __name__=="__main__":
    main()
