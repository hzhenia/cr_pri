from . import regpattern
import re

def extract_disp(line):
    res = []
    return res
    line = line.upper()
    re_pat = re.compile(regpattern.OS_PATTERN,re.IGNORECASE)
    found = re_pat.findall(line)
    for r in found:
        res.append(r)
    return res
def extract_os(line):
    res = []
    line = line.upper()
    re_pat = re.compile(regpattern.OS_PATTERN,re.IGNORECASE)
    found = re_pat.findall(line)
    for r in found:
        res.append(r)
    return res
def extract_tect(line):
    res = []
    line = line.upper()
    re_pat = re.compile(regpattern.TECH_PATTERN,re.IGNORECASE)
    found = re_pat.findall(line)
    for r in found:
        res.append(r)
    return res
def extract_memtype(line):
    res = []
    line = line.upper()
    re_pat = re.compile(regpattern.MEMTYPE_PATTERN,re.IGNORECASE)
    found = re_pat.findall(line)
    for r in found:
        res.append(r)
    return res
def extract_port(line):
    res = []
    line = line.upper()
    re_pat = re.compile(regpattern.PORT_PATTERN,re.IGNORECASE)
    found = re_pat.findall(line)
    for r in found:
        res.append(r)
    return res
def extract_cpu(line):
    res = []
    line = line.upper()
    re_pat = re.compile(regpattern.CPU_PATTERN,re.IGNORECASE)
    found = re_pat.findall(line)
    for r in found:
        res.append(r)
    return res
def extract_brand(line):
    res = []
    line = line.upper()
    re_pat = re.compile(regpattern.BRAND_PATTERN,re.IGNORECASE)
    found = re_pat.findall(line)
    for r in found:
        res.append(r)
    return res
def extract_supplier(line):
    res = []
    line = line.upper()
    re_sup = re.compile(regpattern.SUPPLIER_PATTERN,re.IGNORECASE)
    found = re_sup.findall(line)
    for r in found:
        res.append(r)
    return res
def extract_speed(line):
    res = []
    re_cpu=re.compile('[^\d](\d+[\.,]{0,1}\d*)(.{0,1}hz)',re.IGNORECASE)
    found = re_cpu.findall(line)
    for match in found:
        speed = float(match[0].replace(',','.'))
        dvt =match[1].replace(' ','').upper()
        if dvt == 'GHZ':
            speed = speed *1000
        elif dvt == 'HZ':
            #only in case of 50,60hz (voltage) otherwise due to error type
            #heuristic correction
            if speed == 50.0 or speed==60.0:
                speed = speed/1000
            elif speed < 10: #error type Ghz-> Hz
                speed  = speed * 1000
        elif dvt == 'MHZ':
            if speed <10:
                speed = speed * 1000

        #res.append([speed,match[0],match[1]])
        res.append(speed)
    return res
def get_feature(line):
   #return list of fix size
   Nfeat = 32
   res =[0] * Nfeat
   #CPU types
   cpulst = extract_cpu(line)  #0-3
   speedlst = extract_speed(line) #4-7
   memlst = extract_memtype(line) #8-11
   brandlst = extract_brand(line) #12-15
   portlst = extract_port(line)#16-20
   tectlst = extract_tect(line) #21-23
   displst = extract_disp(line) #24-16j
   oslst = extract_os(line) #27-28
   suplst = extract_supplier(line) #29-32
   print cpulst
   print speedlst
   print memlst
   print brandlst
   print portlst
   print tectlst
   print displst
   print oslst
   print suplst
   for i in range(0,Nfeat):
       if i < 4:
           res[i] = cpulst[i] if i< len(cpulst) else 0
       elif i < 8:
           res[i] = speedlst[i-4] if i-4< len(speedlst) else 0
       elif i < 12:
           res[i] = memlst[i-8] if i-8 < len(memlst) else 0
       elif i < 16:
           res[i] = brandlst[i-12] if i-12< len(brandlst) else 0
       elif i < 21:
           res[i] = portlst[i-16] if i-16< len(portlst) else 0
       elif i < 24:
           res[i] = tectlst[i-21] if i-21< len(tectlst) else 0
       elif i < 27:
           res[i] = displst[i-24] if i-24< len(displst) else 0
       elif i < 29:
           res[i] = oslst[i-27] if i-27< len(oslst) else 0
       else:
           res[i] = suplst[i-29] if i-29 < len(suplst) else 0
   return res
