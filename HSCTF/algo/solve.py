import os 
import sys
from pwn import *

host = 'not-really-math.hsc.tf'
port = 1337
r = remote(host,port)

def solver(j):
    j = j.replace('a', '+')
    k = j.replace('m', ')*(')
    return eval('(('+k+'))') % (pow(2,32)-1)

    
    
r.recvline()
for i in range(15):
    subject = r.recvline().decode('UTF-8')
    if ':' in subject:
        subject = subject[1:]
        if 'flag{' in subject : 
            print("Flag found : {}".format(subject))
            exit()
    log.warning("Problem : {}".format(subject))
    ans = solver(subject)
    log.success("Answer : {}".format(ans))
    r.sendline(str(ans))