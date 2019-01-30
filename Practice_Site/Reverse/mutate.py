
#s=[0x6D,0x58,0x64,0x4A,0x56,0x56,0x52,0x64,0x7C,0x6F,0x51,0x59,0x1F,0x7B,0x4B,0x5D,0x63,0x54,0x6D,0x6B,0x04,0x47,0x69,0x06,0x6B,0x66,0x4C,0x08,0x6E,0x64,0x61,0x5A,0x74,0x32,0x3B,0x1C,0x02,0x2A,0x14,0x18,0x25,0x7A,0x37,0x4B,0x4C,0x4D,0x4E,0x4F,0x50,0x51]
s=['6D','58','64','4A','56','56','52','64','7C','6F','51','59','1F','7B','4B','5D','63','54','6D','6B','04','47','69','06','6B','66','4C','08','6E','64','61','5A','74','32','3B','1C','02','2A','14','18','25','7A','37','4B','4C','4D','4E','4F','50','51']
#s=['6D','58','64','4A','56','56','52','64','7C','6F','51','59','1F','7B','4B','5D','63','54','6D','6B','04','47','69','06','6B','66','4C','08','6E','64','61','5A','74','32','3B','1C','02','2A','14','18','25','7A','37']
flag=[]
hexresult=[]
result=[]
for i in range(0,50):
	decimalval=int(s[i],16)
	#print(decimalval)
	i1=i+32
	ans=decimalval^i1 # decimal 
	#print(ans)
	flag.append(ans) # flag list is decimal 

# convert flag from decimal to hex
for i in range(len(flag)):
	hexflag=hex(flag[i])
	# convert flag from hex to ascii
	asciiflag=chr(int(hexflag, 16))
	hexresult.append(hexflag)
	result.append(asciiflag)

print(flag)
print(hexresult)
print(result) 
'''
a=''
for i in result:
	a += result[i]
'''

#MyFirstCTF{r3VerSe_X0r_1S_v3RY_e4sy_FoR_m3}