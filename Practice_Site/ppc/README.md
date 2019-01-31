# PPC-CTF

- [Calculator](#calculator)
- [Temperature](#temperature)
- [Alphabet](#alphabet)
- [pi](#pi)
- [get-the-root](#root)
- [hurry up](#hurry)
- [lambda](#lambda)

<h2 id=calculator>Calculator</h2>

- 題目

![](/ppc/pic/calculator1.png)
- nc 去看題目內容

![](/Practice_Site/ppc/pic/calculator2.png)
- 該題要能判斷題目給的數值，並回應是要給予+ /- or *
- 會使用python 套件 pwntools
    - pwntools 用於解決將題目讀回來以及把答案送回去使用
- 下方為本題的解題程式
```
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
```
- Get flag : MyFirstCTF{QLwxhEsyUfKQrYxyEeFe}
- 該題的解題過程，一開始會不太知道要如何去判斷 + / - / *
- 但想通後其實不太難。

<h2 id=temperature>Temperature</h2>
 

- 題目

![](/Practice_Site/ppc/pic/temperature1.png)
- nc 去看題目內容

![](/Practice_Site/ppc/pic/temperature2.png)
- 該題要計算華氏轉攝氏，需要寫出一支華氏轉攝氏的程式
- 會使用python 套件 pwntools
    - pwntools 用於解決將題目讀回來以及把答案送回去使用
- 下方為本題的解題程式
```
from pwn import *

context(arch='i386', os='linux')

r=remote('140.110.112.29',5127)# remote connection create
r.recvuntil("Celsius : ")#read 題目到特定位置

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
```

- Get flag : MyFirstCTF{h4rRy potTer anD tHe phiL0sOph3r's TeMper4tuRe}

<h2 id=alphabet>Alphabet</h2>

- 題目

![](/Practice_Site/ppc/pic/alphabet1.png)
- nc 去看題目內容

![](/Practice_Site/ppc/pic/alphabet2.png)

- 這題重點要***算出一個長字串中特定字元的數量***
- 其實就是在考字串的處理，這在python 中有套件能夠套用直接解決
- 但如果真的要探究計算的話，可能要知道怎麼樣切割字串然後一個一個比對，這樣其實要寫蠻長
- 目前是採用python 的count 去計算
- count 用於計算字符串里某个字符出现的次数。可选参数为在字符串搜索的开始与结束位置
- 會使用python 套件 pwntools
    - pwntools 用於解決將題目讀回來以及把答案送回去使用
- 下方為本題的解題程式
```
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
```

- [Python count()方法](http://www.runoob.com/python/att-string-count.html)

<h2 id=pi>pi</h2>

- 題目

![](/Practice_Site/ppc/pic/pi1.png)
- nc 去看題目內容

![](/Practice_Site/ppc/pic/pi2.png)

- 這題有點小小的bug，先來描述一下題目
- 題目要求要算出pi 的值道題目指定的位數
- 但這題的問題是有四捨五入的問題，基本上要求的位數的最後一個數字的值是否要進行四捨五入，要從最後一位在往下判斷一個位數，也就是要***比題目要求的位數在多讀一個位數的意思***
- 那這題的解法可以有兩種:
    1. 自行建立位數表，然後進行查表
    2. 直接找公式進行運算
- 會使用python 套件 pwntools
    - pwntools 用於解決將題目讀回來以及把答案送回去使用
- 下方為本題的解題程式
```
# -*- coding: utf-8 -*-
from __future__ import division
from pwn import *
#import time


context(arch='i386', os='linux')

r=remote('140.110.112.29',5130)
r.recvuntil("3.1415\n")
'''
f= open("circle.txt","r") # read file
pitable=f.read() # read file 
circlepi=re.sub(r"\s+", "",pitable) # remove space 

f2=open("circle2.txt","w") # write file 
f2.write(circlepi) # write file 
'''
for i in range(100):
	r.recvline()
	a=r.recvline()
	b=re.findall("L \= (.*)",a)
	print(b)
	L=int(b[0])+2
	print(L)
	
	f3=open("circle2.txt","r")
	ans=f3.read(L)
	#ans1=int(ans.strip(.)) # remove . and convert to integer
	print('debug:' + ans)
	#print('outside')
	#print('more 1 byte:'+ans[-1])
	lastchar=int(ans[-1])
	if lastchar < 5:
		print('less than 5')
		print('more 1 byte:'+ans[-1])
		result = ans[:-1]
		print('less than 5:'+result)
	else:
		print('more than 5\n')
		print('more 1 byte:'+ans[-1])
		#anslast=str(int(ans[-2])+1)
		#print('anslast:'+anslast)
		ans1=ans[:-1]
		ans1=re.sub('[.]', '',ans1)
		print('asn1:'+ans1)
		ans1=int(ans1) # remove . and convert to integer
		#ans=ans[:-2]
		ans=str(ans1+1)
		print('ans:'+ans)
		#ans=ans+anslast
		result=str(ans)
		result=result[:1]+'.'+result[1:]
		print('result:'+result)
	#print(ans)
	#result=str(ans)
	#result=result[:1]+'.'+result[1:]
	'''
	if L >=	2 :
		L=L+1
	print(L)	
	'''
	
	'''
	# 計算pi
	L1=L+10
	number=10**L1
	x1=number*4//5 # 求含4/5的首项
	x2=number//-239 # 求含1/239的首项
	# 求第一大项
	he=x1+x2
	#设置下面循环的终点，即共计算n项
	#L *=2
	for j in xrange(3,L,2):
		x1//=-25
		x2//=-57121
		x=(x1+x2)//j
		he += x
	ans = he * 4
	ans //= 10**10
	anspi=str(ans)
	print(anspi)
	result=anspi[0]+str('.')+anspi[1:len(anspi)]
	print(result)
	'''
	try:
		r.sendline(result)
	except:
		r.recvline()
	#print(result)
	#print(i)
	i=i+1
	#print(i)


d=r.recvall()
print(d)
```
- 其實這一題有點bug ，對於四捨五入的判斷上花了蠻多時間去處理，但bug 在於碰到題目要求 31 位與48位的pi值時會不需要進行四捨五入，在這一點花了一些時間釐清
- 但其實上面的code 並沒有額外針對31及48這兩個題目另外做判斷!!(太麻煩懶得再寫~)

- [python -pi 計算公式](https://blog.csdn.net/u013421629/article/details/72640062)
- [python - pi 計算](https://www.oschina.net/translate/computing-pi-with-python)

<h2 id=root>get-the-root</h2>

- 題目

![](/Practice_Site/ppc/pic/root1.png)
- nc 去看題目內容

![](/Practice_Site/ppc/pic/root2.png)
- 該題會給予一串數值，並要求將該串值組成多次方程式，並解其根(root)
- 同樣要寫程式去解根
- 使用python 的兩個套件 pwntools、sympy
    - pwntools 用於解決將題目讀回來以及把答案送回去使用
    - sympy 用於解方程式 
- 下方為本題的解題程式
```
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


```
- 執行上面的程式後，會得到flag
- Get flag: MyFirstCTF{RoOt w4rs VIII - th3 L4sT j3dI}
- 解題過程的問題
    1. 如何把去得的題目數值購造成方程式
    2. 在使用recvuntil()時，忘了把換行符號也讀進去，所以必須執行一次recvline()


<h2 id=hurry>hurry up</h2>

- 題目

![](/Practice_Site/ppc/pic/hurry1.png)
- nc 去看題目內容

![](/Practice_Site/ppc/pic/hurry2.png)
- 該題主要就是在實作凱薩加密，會給一段被位移過的英文句子，也會給位移的位數(key)
- 想辦法把原始句子算出
- 會使用python 套件 pwntools
    - pwntools 用於解決將題目讀回來以及把答案送回去使用
- 下方為本題的解題程式
```
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
```
- 該題的重點其實一直都是在字元的判斷上
- 但中間遇到的困難是在A-Z轉換成十進制後，進行shift運算時若超出A-Z的範圍該如何解決
- 這方面基本上直接找Caesar Cipher 的實作可以蠻清楚找到答案

![](/Practice_Site/ppc/pic/hurry3.png)
- [凱薩加密](https://inventwithpython.com/chapter14.html)

<h2 id=lambda>lambda</h2>

- 題目
![](/Practice_Site/ppc/pic/lambda1.png)
- nc 去看題目內容

![](/Practice_Site/ppc/pic/lambda2.png)
- 本題重點:
    1. 判斷題目給的5條式子
    2. 判斷題目要求用哪條式子解題
    3. 判斷題目給的x 值
- 使用python 的兩個套件 pwntools、sympy
    - pwntools 用於解決將題目讀回來以及把答案送回去使用
    - sympy 用於解方程式 

- 下方為本題的解題程式

```
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
```
- 上述解法不是最好的，因為5條式子的判斷沒有完成，是直接hardcode 在程式碼中
- 同時也無法把x值帶入5條式子中
- 網路上有查詢到用python lambda 的方式感覺可以用來implement 該題
- [lambda replace switch case on python](https://simonwillison.net/2004/May/7/switch/)
- [lambda 運算式](https://openhome.cc/Gossip/Python/LambdaExpression.html)

![](/Practice_Site/ppc/pic/lambda3.png)

## 相關實用Knowledge 
```
pwntools 
sympy 
hex 
ord 
int()
```

## Reference 

- [使用 sympy 解聯立方程組](http://blog.float.tw/2013/04/using-sympy-solve-simultaneous-equations.html)
- [python ord 函數](http://www.runoob.com/python/python-func-ord.html)
- [Python split()方法__用空白切字串](http://www.runoob.com/python/att-string-split.html)
- [How do I convert hex to decimal in Python? [duplicate]](https://stackoverflow.com/questions/9210525/how-do-i-convert-hex-to-decimal-in-python)
- [[Python] range() 與 xrange()的比較](http://falldog7.blogspot.com/2009/07/python-range-xrange.html)
- [Python xrange() 函数](http://www.runoob.com/python/python-func-xrange.html)
- [Python - int, hex, char, string的轉換](http://mini-stable.blogspot.com/2015/03/python-int-hex-char-string.html)
- [hex & decimal convert online](https://www.rapidtables.com/convert/number/hex-to-decimal.html?x=7d)
- [Hex and ASCII text converter online](https://www.rapidtables.com/convert/number/hex-to-ascii.html)
- [ASCII码对照表](http://ascii.911cha.com)
- [Decimal ASCII Chart](http://www.asciichart.com/)
- [pwntools install](http://docs.pwntools.com/en/stable/install.html)
- [pwntools使用简介](https://blog.csdn.net/qq_29343201/article/details/51337025)
- [pwntools install 中文](https://pwntoolsdocinzh-cn.readthedocs.io/en/master/intro.html)
- [pwntools使用簡介2](https://tw.saowen.com/a/8d2699263a54fdc12eb7a613fb9fbf8d7c3d4f0b730db162a7c55b71c3555a4a)
- [正規表達示 re_findall](https://www.cnblogs.com/xieshengsen/p/6727064.html)
- [圓周率](https://zh.wikipedia.org/zh-tw/%E5%9C%93%E5%91%A8%E7%8E%87)
- [如何計算圓周率 Pi](https://zh.wikihow.com/%E8%AE%A1%E7%AE%97%E5%9C%86%E5%91%A8%E7%8E%87-Pi)
###### tags: `CTF` `PPC`
