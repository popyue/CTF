

encrypt = 'HITSS{5X65Z1ZXZ10F_E1LI3J}'
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ{}_1234567890'
key   = 'QWERTPOIUYASDFGLKJHZXCVMNB{}_1234567890'

plain = ''
for i in encrypt:
	print('i=' + i)
	index = key.index(i)
	print('index=' . index)
	plain += alpha[index]
	print('plain= ' + plain)

print(plain)