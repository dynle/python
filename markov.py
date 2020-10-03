# this script from "AVRマイコンとPythonではじめよう IoTデバイス設計"

import numpy as np

f=open("sazae.txt","r")
lines=f.readlines()
out=open("janken.txt","w")

for i in lines:
    if len(i)>1: out.write(i.split()[2])
out.close()

f=open("janken.txt","r")
lines=f.readlines()

g="グー"
c="チョキ"
p="パー"

m=np.array([g,c,p])

def op1(x):
    for i in x:
        for j in lines:
            print(i,"=",j.count(i))

def op2(x,y):
    for i in x:
        for j in y:
            for k in lines:
                print(i+j,"=",k.count(i+j))

def op3(x,y,z):
    for i in x:
        for j in y:
            for k in z:
                for l in lines:
                    print(i+j+k,"=",l.count(i+j+k))

op1(m)
op2(m,m)
op3(m,m,m)