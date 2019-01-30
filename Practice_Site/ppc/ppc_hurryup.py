# -*-coding:utf-8 -*-

from pwn import *

context(arch='i386', os='linux')

r=remote('140.110.112.29',5123)# remote connection create
r.recvuntil("Hurry up, winter is coming...\n")
for i in range(100):
	r.recvline()
	a=r.recvline()
	#print('a',a)
	b=re.findall("shift every alphabet in the word by (.*) : (.*)",a)
	print('b',b)
	alphabet=b[0][1]
	decimallist=[]
	# 判斷題目字串
	for l in range(len(alphabet)):
		#print(type(alphabet[i]))
		alphabet1=alphabet[l]
		#alphahex=hex(ord(alphabet1))
		#alphadecimal=int(alphahex,16)
		alphadecimal=ord(alphabet1)
		decimallist.append(alphadecimal)
	print('decimal:',decimallist)
	#print('alphahex:',alphahex)
	#print('alphadecimal',alphadecimal)
	shiftnum=b[0][0]
	#print(shiftnum)
	shiftlist=[]
	ans=''
	# Caesar Cipher 實作
	for j in range(len(decimallist)):
		if decimallist[j] >= 65 and decimallist[j] < 91:  
			shiftalpha=decimallist[j]+int(shiftnum)
			#print('out:',shiftalpha)
			#print(type(shiftalpha))
			if shiftalpha > ord('Z'):
				#print('big:',shiftalpha)
				shiftalpha -= 26
				shiftlist.append(shiftalpha)
			elif shiftalpha < ord('A'):
				#print('small:',shiftalpha)
				shiftalpha += 26
				shiftlist.append(shiftalpha)
			else:
				#shiftlist.append(shiftalpha)
		else:
			#print('j:',j)
			#print('else:',decimallist[j])
			#print('decimallist[j]:',decimallist)
			shiftlist.append(decimallist[j])
			#print('shiftlist[j]:',shiftlist) 
	#print('shiftlist:',shiftlist)
	# 組合結果
	for k in range(len(shiftlist)):
		resultstr=chr(shiftlist[k])
		ans=ans+resultstr
	result=str(ans)
	r.sendline(result)
	i=i+1

flag=r.recvall()
print(flag)