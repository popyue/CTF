Cipher = "HESL{LRAT5PN51010T_CNPH1R}3"

key=[3,1,2]
Cipher_size = len(Cipher)
print Cipher_size

li1=[]
li2=[]
li0=[]

for i in range(0, Cipher_size):
	if i%3 == 0:
		li1.append(Cipher[i])
	if i%3 == 1:
		li2.append(Cipher[i])
	if i%3 == 2:
		li0.append(Cipher[i])

print(li1)
print(li2)
print(li0)

ans = []
for i in range(len(li1)):
	ans.append(li0[i])
	ans.append(li1[i])
	ans.append(li2[i])

print(ans)
Plain_text = (''.join(ans))
print(Plain_text)