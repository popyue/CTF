# -*-coding:utf-8 -*-

from pwn import *

context(arch='i386', os='linux')

r=remote('140.110.112.29',5127) # remote connection create
r.recvuntil("Celsius : ") #read 題目到特定位置

for i in range(100):
	a=r.recvuntil("Celsius : ")
	b=re.findall("Fahrenheit : (.*)\n",a)# 正規表示取得題目給的華氏溫度度數
	print(b)
	# 華氏轉攝氏code
	c=(int(b[0])-32)*5
	print(c)
	r.sendline(str(c)+'/9')#Send Answer back
	i=i+1
d=r.recvall()
print(d)