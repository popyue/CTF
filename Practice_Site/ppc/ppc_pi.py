# -*- coding: utf-8 -*-
from __future__ import division
from pwn import *
#import time


context(arch='i386', os='linux')

r=remote('140.110.112.29',5130)
r.recvuntil("3.1415\n")
'''
f= open("circle.txt","r") # read file
pitable=f.read() # read file 
circlepi=re.sub(r"\s+", "",pitable) # remove space 

f2=open("circle2.txt","w") # write file 
f2.write(circlepi) # write file 
'''
for i in range(100):
	r.recvline()
	a=r.recvline()
	b=re.findall("L \= (.*)",a)
	print(b)
	L=int(b[0])+2
	print(L)
	
	f3=open("circle2.txt","r")
	ans=f3.read(L)
	#ans1=int(ans.strip(.)) # remove . and convert to integer
	print('debug:' + ans)
	#print('outside')
	#print('more 1 byte:'+ans[-1])
	lastchar=int(ans[-1])
	if lastchar < 5:
		print('less than 5')
		print('more 1 byte:'+ans[-1])
		result = ans[:-1]
		print('less than 5:'+result)
	else:
		print('more than 5\n')
		print('more 1 byte:'+ans[-1])
		#anslast=str(int(ans[-2])+1)
		#print('anslast:'+anslast)
		ans1=ans[:-1]
		ans1=re.sub('[.]', '',ans1)
		print('asn1:'+ans1)
		ans1=int(ans1) # remove . and convert to integer
		#ans=ans[:-2]
		ans=str(ans1+1)
		print('ans:'+ans)
		#ans=ans+anslast
		result=str(ans)
		result=result[:1]+'.'+result[1:]
		print('result:'+result)
	#print(ans)
	#result=str(ans)
	#result=result[:1]+'.'+result[1:]
	'''
	if L >=	2 :
		L=L+1
	print(L)	
	'''
	
	'''
	# 計算pi
	L1=L+10
	number=10**L1
	x1=number*4//5 # 求含4/5的首项
	x2=number//-239 # 求含1/239的首项
	# 求第一大项
	he=x1+x2
	#设置下面循环的终点，即共计算n项
	#L *=2
	for j in xrange(3,L,2):
		x1//=-25
		x2//=-57121
		x=(x1+x2)//j
		he += x
	ans = he * 4
	ans //= 10**10
	anspi=str(ans)
	print(anspi)
	result=anspi[0]+str('.')+anspi[1:len(anspi)]
	print(result)
	'''
	try:
		r.sendline(result)
	except:
		r.recvline()
	#print(result)
	#print(i)
	i=i+1
	#print(i)


d=r.recvall()
print(d)