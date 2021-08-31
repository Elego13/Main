#evan jurdan
import subprocess
import sys
import os
import csv
#print("hi")
try:
    filee = sys.argv[1]
except IndexError:
    print("error need a file inputed as an argument")
    exit(1)

logg = []
ipz = []
noomz = []
counIP = []

def read(fil, loog, ips, noom):
    inn=open(fil, 'r')
    line = inn.readline().strip()
    run = True
    while run:
        line = inn.readline().strip()
        split= line.split(" ")
        if(not line):
            run = False
        else:
            #print(line)
            List = []
            List.append((split[0]))
            List.append((split[1]))
            List.append((split[2]))
            List.append((split[3]))
            List.append((split[4]))
            List.append((split[5]))
            List.append((split[6]))
            
            
            #print(List)
            test = split[5]+" "+split[6]
            if test == "Failed password":
                loog.append(List)
                runn = True
                nu=7
                while runn:
                    try:
                        ttes = split[nu]
                    except IndexError:
                        runn=False
                    if ttes == "from":
                        iippz = split[(nu+1)]
                        noom.append(iippz)
                    nu = nu + 1
                exis = False
                for i in ips:
                    if i == iippz:
                        exis = True 
                
                if exis == False:
                    ips.append(iippz)
                    #print(split[2])
                #print(iippz)


def count_ips(ips, noom, CI):
    
    for i in ips:
        runn = True
        count = 0
        for x in noom:
            if i == x:
                count = count + 1

        #print(str(i)+" "+str(count))
        if count >= 10:
            app = []
            app.append(count)
            app.append(i)
            process = subprocess.Popen(['geoiplookup', str(i)], stdout=subprocess.PIPE, universal_newlines=True)
            output = process.stdout.readline()
            begin = output.find(',') + 2
            end = output.find('\n')
            Loc = output[begin:end]
            #print(Loc)
            #Loc = " "
            app.append(Loc)
            CI.append(app)

            
def sortt(CI):
    runn = True
    CI.sort(reverse=True,key=tkfir)
    #print(CI)


def tkfir(elem):
    return elem[0]


def prnt(CI):
    
    print("Count, IP, Location")
    for i in CI:
        print(str(i[0])+", "+str(i[1])+", "+str(i[2]))


def wrt(CI):
    fil= filee+"attempts.csv"
    with open(fil, mode='w') as _file:
        writer = csv.writer(_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['Count','IP','Location'])
        for i in CI:
            writer.writerow([str(i[0]),str(i[1]),str(i[2])])

read(filee, logg, ipz, noomz)
count_ips(ipz, noomz, counIP)
sortt(counIP)
prnt(counIP)
wrt(counIP)
#print(logg)
#print(len(logg))
#print(ipz)
#print(counIP)