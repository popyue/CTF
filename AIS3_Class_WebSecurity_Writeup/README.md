# AIS3_Web Security & Hacking hands-on practice_Write up 

## Website:http://www.onesecurity.kr/

* [Paris](#Paris)
* [Madrid](#Madrid)
* [Segovia](#Segovia)
* [Avila](#Avila)
* [Ronda](#Ronda)
* [Bercelona](#Bercelona)
* [Melbourne](#Melbourne)


<h2 id=Paris>Paris</h2>

題目：

    先附上題目圖片：
![Parisimg](/AIS3_Class_WebSecurity_Writeup/img/Paris.PNG)
    
    由題目可以知道在source code有flag的提示。
    所以直接找source code：
    果然在source code中發現類似提示的註解，寫著：
    
```sh
<!--'ADMIN TEST'/web/admin/admin_login_check.asp?user_id=-->
```
![Parisimg1](/AIS3_Class_WebSecurity_Writeup/img/Paris_1.PNG)

    看到提示後
    當然就是直接修改url到提示上的位置，
    但問題是user_id 是什麼？
    我第一個想到的是先試試看自己的id，
    但這個一定不會過，
    後來想說他是要admin login check，
    那就試試看admin吧！！
    
    **一試就中～～**
![Parisimg2](/AIS3_Class_WebSecurity_Writeup/img/Paris_2.PNG)

    進去之後，同樣的開啟source code，
    會看到一個被hidden起來的input box，
    裡面有一串被編碼過的字串，
    結尾兩個等於（==）看起來就像是 base64。
![Parisimg3](/AIS3_Class_WebSecurity_Writeup/img/Paris_3.PNG)
    
    丟進解碼器解碼後得到flag!!!
![Parisimg4](/AIS3_Class_WebSecurity_Writeup/img/Paris_4.PNG)
    

<h2 id=Madrid>Madrid</h2>

題目：

    先附上題目圖片：
![Madridimg](/AIS3_Class_WebSecurity_Writeup/img/Madrid.PNG)
    
    這題提到密碼要先找到一個file，
    而file name 的提示是
    iphone root default password
    所以直接google 
    iphone root default password
    
![Madridimg1](/AIS3_Class_WebSecurity_Writeup/img/Madrid_1.PNG)
    
    google 到一個可能的 ‘alpine’
    key 上 url 試試。

    
![Madridimg2](/AIS3_Class_WebSecurity_Writeup/img/Madrid_2.PNG)

    flag 噴出拉！！
![Madridimg3](/AIS3_Class_WebSecurity_Writeup/img/Madrid_3.PNG)


<h2 id=Segovia>Segovia</h2>

題目：

    先附上題目圖片：
![Segoviaimg](/AIS3_Class_WebSecurity_Writeup/img/Segovia.PNG)

    題目告知有一個 login site，
    以及一個 Keyword，
    進入login site
![Segoviaimg1](/AIS3_Class_WebSecurity_Writeup/img/Segovia_1.PNG)

    key 上 keyword，但出現以下錯誤。
    **字串過長**
    限制字串要在8個字以內。
![Segoviaimg2](/AIS3_Class_WebSecurity_Writeup/img/Segovia_2.PNG)

    看到著個想得到的事source code 
    可能有地方在限制可以輸入的字數
    由於html 的input box 輸入已經超過8 個字
    而且有跳出彈出視窗所以可能不是靜態的code，
    所以排除了html，
    接著檢查 javascript。
![Segoviaimg3](/AIS3_Class_WebSecurity_Writeup/img/Segovia_3.PNG)

    果然找到js 中有著限制長度的部分。
![Segoviaimg4](/AIS3_Class_WebSecurity_Writeup/img/Segovia_4.PNG)
    直接把長度加到20。
![Segoviaimg5](/AIS3_Class_WebSecurity_Writeup/img/Segovia_5.PNG)
    flag 噴出拉～～～


<h2 id=Avila>Avila</h2>

題目：

    先附上題目圖片：
![Avilaimg](/AIS3_Class_WebSecurity_Writeup/img/Avila.PNG)
    
    這題我覺得比較麻煩，
    題目是敘述說有一個使用者叫 ‘anesra’
    他的這題已通過，在他的帳號上有這題的password
    
![Avilaimg1](/AIS3_Class_WebSecurity_Writeup/img/Avila_1.PNG)
    
    想著要如何登入 ‘anesra’
    這裡的方法是用修改cookie
    
![Avilaimg2](/AIS3_Class_WebSecurity_Writeup/img/Avila_2.PNG)
    
    把 userid 的部分改成 'anesra'
    確實登入 'anesra'
    果然登入後有著 password
![Avilaimg3](/AIS3_Class_WebSecurity_Writeup/img/Avila_3.PNG)
![Avilaimg4](/AIS3_Class_WebSecurity_Writeup/img/Avila_4.PNG)
![Avilaimg5](/AIS3_Class_WebSecurity_Writeup/img/Avila_5.PNG)

    但這邊如果照著password 打還是有問題不會過
    看了後面沒過的頁面發現自被截斷只剩下
    CastleW
    程市大概有針對某些字串進行過濾
    ex. all
    所以最後 key 上 CastleWaallll
    讓他把all截斷後剩下的就是flag

![Avilaimg6](/AIS3_Class_WebSecurity_Writeup/img/Avila_6.PNG)


<h2 id=Ronda>Ronda</h2>

題目：

    先附上題目圖片：
![Rondaimg](/AIS3_Class_WebSecurity_Writeup/img/Ronda.PNG)
    
    題目描述有個admin login page 藏著
    一開始以為是 admin_login.asp
    但不對
![Rondaimg](/AIS3_Class_WebSecurity_Writeup/img/Ronda_1.PNG)
    
    後來試試 /admin/login.asp
    成功找到頁面，
    出現一個登入畫面
![Rondaimg2](/AIS3_Class_WebSecurity_Writeup/img/Ronda_2.PNG)
![Rondaimg3](/AIS3_Class_WebSecurity_Writeup/img/Ronda_3.PNG)
    
    再登入畫面，
    首先試試看 sql injection
    (講師才剛講過的！！)
    ‘ or ''='

![Rondaimg4](/AIS3_Class_WebSecurity_Writeup/img/Ronda_4.PNG)

    果然成功get flag~~~
    
    
<h2 id=Bercelona>Bercelona</h2>

題目：

    先附上題目圖片：
![Bercelonaimg](/AIS3_Class_WebSecurity_Writeup/img/Bercelona.PNG)
    
    此題困擾我蠻久，
    題目敘述正解是一個地名，
    還特別說了要大寫並排除底線，
    一開啟看到sniffing message，
    第一個想到的還是 base64 
![Bercelonaimg1](/AIS3_Class_WebSecurity_Writeup/img/Bercelona_1.PNG)

    帶進decode 後得到一個wiki 的頁面，
    看了wiki好久，
    找了好久裡面的地名
    第一個就試 Sagrad Familia
    但自己是錯，中間夾了的空白
    所以之後找了蠻久
![Bercelonaimg2](/AIS3_Class_WebSecurity_Writeup/img/Bercelona_2.PNG)
    
    最後去掉空白，拿到flag!!!!
    
    
<h2 id=Melbourne>Melbourne</h2>

題目：

    先附上題目圖片：
![Melbourneimg](/AIS3_Class_WebSecurity_Writeup/img/Melbourne.PNG)

    這題又是考驗google拉
    題目說facebook 創辦人的twitter密碼
    因為twitter被駭而流出。
    而密碼藏在特別的file，
    file name 就是佐伯克twitter 密碼
![Melbourneimg1](/AIS3_Class_WebSecurity_Writeup/img/Melbourne_1.PNG)

    上網google後，找到dadada
![Melbourneimg2](/AIS3_Class_WebSecurity_Writeup/img/Melbourne_2.PNG)

    立刻試試dadada.txt 在url 上
![Melbourneimg3](/AIS3_Class_WebSecurity_Writeup/img/Melbourne_3.PNG)

    GET FLAG!!!
