
chartable=[]
for j in range(32,128):
	ans=(j+13)%95+32
	chartable.append(ans)
print(chartable)

s='zGs7@ABp"sIp/3bn@-:A-G]CllNNK'
decimalstack=[]
#print(len(s))
for i in range(len(s)):
	a=s[i]
	hexvalue=hex(ord(a))
	#print(hexvalue)
	decimalval=int(hexvalue,16)
	#print(decimalval)
	decimalstack.append(decimalval)
print(decimalstack)

s1=[77,121,70,105,114,115,116,67,84,70,123,67,97,101,53,65,114,95,108,115,95,121,48,117,63,63,33,33,125]
s2=[]
for l in range(len(s1)):
	z=hex(s1[l])
	print(z)
	s2.append(z)

print(s2)