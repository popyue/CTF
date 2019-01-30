# -*-coding:utf-8 -*-

from pwn import *
from sympy import *
import re


r=remote('140.110.112.29',5124)
r.recvuntil("here is some functions f\n")
r.recvline() # f0(x)=3x^2 + x + 3
r.recvline() # f1(x) = 5x^2 + 8
r.recvline() # f2(x) = 4x^3 + 6x + 6
r.recvline() # f3(x) = 7x^3 + 5x^2
r.recvline() # f4(x) = x^2 + 4x + 3
'''
f0=re.findall("f0(x) = (.*)\^(.*) \+ (.*) \+ (.*)\n",a)
print('f0:',f0)
f1=r.recvline()
f1=re.findall("f1(x) = (.*)",f1)
f2=r.recvline()
f2=re.findall("f2(x) = (.*)",f2)
f3=r.recvline()
f3=re.findall("f3(x) = (.*)",f3)
f4=r.recvline()
f4=re.findall("f4(x) = (.*)",f4)

print('f1:',f1)
print('f2:',f2)
print('f3:',f3)
print('f4:',f4)
'''
'''
functions={
'0':lambda x:f0,
'1':lambda x:f1,
'2':lambda x:f2,
'3':lambda x:f3,
'4':lambda x:f4
}[value](x)
'''
#print(function1)
r.recvuntil("f(x) = 28\n")
sol=0
for i in range(100):
	r.recvline()
	questionline1=r.recvline()
	#print(questionline1)
	foption=re.findall("function : (.*)",questionline1)
	#print('foption:',foption)
	questionline2=r.recvline()
	unknownx=re.findall("x = (.*)",questionline2)
	x=int(unknownx[0])
	#print('x:',x)

	if foption[0] == '0':
		sol=3*(x**2)+x+3
		print('inside:',sol)
	elif foption[0] == '1':
		sol=5*(x**2)+8
		print('inside:',sol)
	elif foption[0] == '2':
		sol=4*(x**3)+6*x+6
		print('inside:',sol)
	elif foption[0] == '3':
		sol=7*(x**3)+5*x**2
		print('inside:',sol)
	elif foption[0] == '4':
		sol=(x**2)+4*x+3
		print('inside:',sol)
	#print('outside:',sol)
	result=str(sol)
	print(result)
	'''
	function={
	'0':lambda x:f0,
	'1':lambda x:f1,
	'2':lambda x:f2,
	'3':lambda x:f3,
	'4':lambda x:f4
	}[foption](x)
	
	print(foption)
	print(x)
	print(function)
	'''

	r.sendline(result)
	i=i+1

d=r.recvall()
print(d)