from pwn import * 

context(arch='i386',os='linux')

r=remote('140.110.112.29',5128)
r.recvuntil("Can you help us?\n")

for i in range(100):
	r.recvline()
	a=r.recvline()
	print(a)
	b=re.findall("How many (.*) in (.*)",a)
	print(b)
	patten=b[0][0]
	string=b[0][1]
	print(patten)
	print(string)
	c=string.count(patten,0,len(string))
	print(c)
	e=str(c)
	r.sendline(e)
	i=i+1

d=r.recvall()
print(d)