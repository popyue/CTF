from pwn import *
from sympy import * 

r=remote('140.110.112.29',5122) # remote connection create
r.recvuntil("root : 1 (just one of the roots, and gurantee to be integer)")
r.recvline() #read 題目(\n)
for i in range(100):
	r.recvline() # read 多於的字串:----- wave : 1/100 -----
	a=r.recvline() # read 要解題的字串
	question=a.split(" ")# 用空白來切分字串
	#print(question)
	polynomial=[]
	for j in range(len(question)):
		if j>1:
			# 要把question list中的前兩個value 過濾掉('Polynomial' & ':'')
			# 剩下的放進polynomial list中
			polynomial.append(question[j]) 
	x=Symbol('x') # sympy 中用來構造出未知數'x'
	polylen=len(polynomial)
	constant=''
	polynomial1=[]
	f=0
	# 開始構造方程式
	for k in range(polylen):
		#print("k:",k)
		if k == polylen-1:
			# 儲存常數項
			constant=polynomial[k]
			polynomial1.append(int(constant))
			#f=f+polynomial[k]
		else:
			#構造多次項及其係數的組合
			polynomial1.append(int(polynomial[k])*x**(polylen-(k+1)))
			#f=f+polynomial1[k]
	polylen1=len(polynomial1)
	for l in range(polylen1):
		f=f+polynomial1[l]
	
	#print(f)
	sol=solve(f,x)# sympy 解方程式
	#print('sol:' ,sol[1])
	solfe=sol[1] # Answer store in the second of list
	result=str(solfe)
	#print(result)
	r.sendline(result)
	#print('AfterSendline:',result)
	i=i+1
	#print('i:',i)


d=r.recvall()
print(d)
