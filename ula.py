#!/usr/bin/python
#-*- coding:utf-8 -*-

import time
import hashlib

ndate=[]
dates=format(int(time.time()),'x')
dates = ":".join(str(dates))
#print dates
dates=dates.split(":")

for num in range(0,8,2):
  ndate.append(dates[num]+dates[num+1])

ntpdate=":".join(ndate)
#print ntpdate 
cmacaddr=[]

print("input MAC")

#macaddr=raw_input(">>")
macaddr="58:55:ca:fb:5a:e9"
#print macaddr

smacaddr=macaddr.split(":")

#print "smacaddr="
#print smacaddr

smacaddr.insert(3,"ff")
smacaddr.insert(4,"fe")
rebit=".".join(smacaddr[0])
rebit=rebit.split(".")
#print rebit
rebitd=format(int(rebit[1]),'b')
#print rebitd
rebits=".".join(rebitd)
#print rebits
rebits=rebits.split(".")


if(int(rebit[1])>=4 and int(rebit[1])<8):
  rebits.insert(0,"0")
elif(int(rebit[1])>1 and int(rebit[1])<4):
  rebits.insert(0,"0")
  rebits.insert(1,"0")
elif(int(rebit[1])==1 or int(rebit[1])==0):
  rebits.insert(0,"0")
  rebits.insert(1,"0")
  rebits.insert(2,"0")


if(int(rebits[2])==1):
  rebits[2]='0'
else:
  rebits[2]='1'

#print rebits
hoge = rebits[0]+rebits[1]+rebits[2]+rebits[3]
#print hoge

#print smacaddr[0]
#print rebit[0]
swap=hex(int(hoge,2))[2:]
#print swap
smacaddr[0]=rebit[0]+str(swap)
#print smacaddr[0]


cache=format(int(smacaddr[0],16),'b')
#print cache
#print hex(int(cache,2))

for i in range(0,8,2):
  cmacaddr.append(smacaddr[i]+smacaddr[i+1])

homu=":".join(smacaddr)

print "EUI-64 : %s"% homu
#print ":".join(cmacaddr)

neui64=ndate+smacaddr

#print neui64

#neui64=":".join(neui64)
neui64="".join(neui64)

#print neui64
ulahash=hashlib.sha1(neui64).hexdigest()
#print ulahash
#print len(ulahash)
ulagro=":".join(ulahash[30:])
#print ulagro
ulagro=ulagro.split(":")
#print ulagro
ulas=[]
for i in range(0,10,2):
  ulas.append(ulagro[i]+ulagro[i+1])

#print ulas

ulas.insert(0,"fd")
#print ulas
myula=[]
for i in range(0,6,2):
  myula.append(ulas[i]+ulas[i+1])

myula=":".join(myula)

print "ULA: %s/64" % myula
