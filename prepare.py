#!/usr/bin/python
import sqlite3
import sys

TRAINING_FILE = "samples.txt"
PRICE_DB = "pricedb.db"


def prepare_db():
    c=sqlite3.connect(PRICE_DB)
    c.execute('''CREATE TABLE if not exists freq_term (term text, freq real)''')
    c.commit()
    c.close()


def extract_freq_term():
    print "extracting term..."
    c = sqlite3.connect(PRICE_DB)
    terms= {}
    f = open(TRAINING_FILE)
    lines = f.readlines()
    total = len(lines)
    i = 0
    for l in lines:
        i=i+1
        print "%d/%d" %(i,total)
        for w in l.split():
            if len(w)>=2:
                terms[w] = terms[w]+1 if w in terms.keys() else 0
    d = []
    for w in terms.keys():
        d.append([w,terms[w]])
    print "inserting into db..."
    c.executemany('''INSERT INTO freq_term (term, freq) VALUES(?,?)''', d)
    c.commit()
    c.close()
    print "extracting finished"
def main():
    prepare_db()
    extract_freq_term()





#run the program:
if __name__ == "__main__":
    main()
