# HSCTF 

- [no right click](#no-right-click)
- [Digits-of-pi](#digits-of-pi)

## Web 

<h3 id='no-right-click'>no right click</h3>


- Site : https://no-right-click.hsc.tf/

![](/HSCTF/img/no-right-click_1.png)


- 網頁原始碼

![](/HSCTF/img/no-right-click_2.png)
![](/HSCTF/img/no-right-click_3.png)

- 跟進 useless-file.css 去看

![](/HSCTF/img/no-right-click_4.png)

- flag : flag{keyboard_shortcuts_or_taskbar}


<h3 id='digits-of-pi'>Digits-of-pi</h3>

- Site : https://docs.google.com/spreadsheets/d/1y7AxYvBwJ1DeapnhV401w0T5HzQNIfrN1WeQFbnwbIE/edit#gid=0

- 這是一個google excel ，但稍微瀏覽一下這個excel 可以發現似乎有隱藏的sheet 

![](/HSCTF/img/digits-of-pi_1.png)

- 再看一下可以用的功能如下
    1. 尋找與取代
    2. 查看 -> 隱藏工作表
    3. 查看 -> 縮放比例
    4. 查看 -> 全螢幕
    5. 資料 -> 排序工作表
    6. 資料 -> 篩選器檢視畫面
    7. 資料 -> 已命名範圍
    8. 資料 -> 受保護的工作表和範圍
    9. 資料 -> 資料欄統計資料
    10. 工具
    11. 說明

- 可用的應該是"尋找與取代"
- 用尋找和取代，搜尋 "flag"

![](/HSCTF/img/digits-of-pi_2.png)

![](/HSCTF/img/digits-of-pi_3.png)


- Flag: flag{hidden_sheets_are_not_actually_hidden}


<h3 id='message-board'>
message-board
</h3>


- Site :　https://message-board.hsc.tf/

- 瀏覽題目網址，是個登入頁面
![](/HSCTF/img/message-board_1.png)
![](/HSCTF/img/message-board_2.png)


- 從題目的敘述可以了解是一個留言板，要找到admin 的權限才能看到被隱藏的內容
![](/HSCTF/img/message-board_0.png)

- 題目僅提供一個一般使用者的帳號username: kupatergent password: gandal
- 先試著login，burp 觀察一下可以發現登入後會有寫入cookie 
- cookie 內容是 username 和 userID 


![](/HSCTF/img/message-board_7.png)

![](/HSCTF/img/message-board_8.png)

![](/HSCTF/img/message-board_9.png)

![](/HSCTF/img/message-board_10.png)

![](/HSCTF/img/message-board_11.png)

- 看一下source code ，可以知道要拿到flag 必須要找到admin 對應的 userID ，已知 kupatergent 的 userID 是 972，暫時可以假設ID 是由3位數組成，也就是說可能的值有1000組，bruteforce 他。

![](/HSCTF/img/message-board_3.png)

![](/HSCTF/img/message-board_4.png)

![](/HSCTF/img/message-board_5.png)

![](/HSCTF/img/message-board_6.png)

![](/HSCTF/img/message-board_12.png)

- 結果在ID:762 可以找到 flag 

![](/HSCTF/img/message-board_13.png)

- flag : flag{y4m_y4m_c00k13s}
- 
![](/HSCTF/img/message-board_16.png)

## Crypto 

- Encryption Code 

![](/HSCTF/img/aptenodytes-forsteri_1.png)

- Decryption Code
 
![](/HSCTF/img/aptenodytes-forsteri_2.png)

- Cipher Text

![](/HSCTF/img/aptenodytes-forsteri_3.png)

- Plain Text 

![](/HSCTF/img/aptenodytes-forsteri_4.png)


- flag : QWERTYUIOP

## Algo 



###### tags: `CTF` `Security` `HSCTF` `2021`