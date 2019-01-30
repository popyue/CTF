from pwn import *

r=remote('140.110.112.29', 5119)# remote connection create
r.recvuntil("Can you help us?\n")#read 題目到特定位置
for i in range(100):
	r.recvline()
	a=r.recvline()
	b=re.findall("(.*) \? (.*) \= (.*)", a) # 正規表示取得題目的數值
	print(b)
	# 把題目的數值分別用變數儲存
	first=b[0][0] 
	second=b[0][1]
	third=b[0][2]
	# 判斷+/-/*
	if int(first) + int(second) == int(third):
		r.sendline('+')
	elif int(first) - int(second) == int(third):
		r.sendline('-')
	else:
		r.sendline('*')
	i=i+1

d=r.recvall()
print(d)