#evan jurdan
import sys
import os
#print("hi")
filee = sys.argv[1]
main = []
construct = []
unique = []
def read(fil, big):
    inn=open(fil, 'r')
    line = inn.readline().strip()
    run = True
    while run:
        line = inn.readline().strip()
        split= line.split(",")
        if(not line):
            run = False
        else:
            #print(line)
            List = []
            List.append(int(split[0]))
            List.append((split[1]))
            List.append((split[2]))
            List.append((split[3]))
            List.append((split[4]))
            List.append((split[5]))
            List.append((split[6]))
            #print(List)
            if not List[0] or not List[1] or not List[2] or not List[3] or not List[5] or not List[6]:
                big.append(("ni",List[0]))
            else:
                big.append(List)
def mak(big, USE, extra):
    num = 0
    run = True
    while run:
        try:
            work = big[num]
        except IndexError:
            run = False
            break
        constr = []
        if work[0] == "ni" or not work:
            #print("can't")
            USE.append(work)
        else:
            #print(work)
            unam = work[2][0]+work[1]+str(work[0])[4]+str(work[0])[5]+str(work[0])[6]
            #print(unam)
            name = work[2]+" "+work[1]
            dep = work[5]
            password = work[0]
            use = []
            use.append(unam)
            use.append(name)
            use.append(dep)
            use.append(password)
            USE.append(use)
            runz=True
            numz = 0
            tryy = 0
            if num == 0:
                extra.append(dep)
            while runz:
                try:
                    test = extra[numz]
                    numz = numz + 1
                except IndexError:
                    runz = False
                    break              
                if test == dep:
                    truet = True
                    tryy = tryy + 1
                else:
                    tryy = tryy
            if tryy != 1:
                copy = False
                extra.append(dep)
            
                


            
        num = num + 1

def addd(Buil, uni):
    run=True
    num = 0
    runz=True
    numz = 0
    while runz:
        try:
            test = uni[numz]
        except IndexError:
            runz = False
            break
        os.system("groupadd -f "+test)
        numz = numz + 1

    

    while run:
        try:
            work = Buil[num]
            #print(work)
        except IndexError:
            run = False
            break
        if work[0] == "ni":
            print("BAD RECORD: EmployeeID= "+str(work[1]))

        elif work[2] == "office":
            os.system("useradd -m -d /home/office/"+work[0]+" -s /bin/css -g office -c "+'"'+work[1]+'" '+work[0])
            os.system("passwd --stdin "+work[0])
            os.system("passwd -e "+work[0])
        else:
            os.system("useradd -m -d /home/"+work[2]+"/"+work[0]+" -s /bin/bash -g office -c "+'"'+work[1]+'" '+work[0])
        
        




        num = num + 1




read(filee, main)
mak(main, construct, unique)
addd(construct, unique)
#print(main)
