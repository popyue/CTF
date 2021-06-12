# SHELL CTF

## Outline 

### Web Security

1. [Collide](#collision)
2. [Fun With Token](#FunWithToken)
3. [Login](#login)

## Information

- [Site](https://shellctf.games/challenges)


## Web Security 題目

<h3 id='collision'> Collide </h3>

Link of Problem : http://3.142.122.1:9335/

![](/SHELLCTF/pic/Collision_1.png)

- Payload 

``` http://3.142.122.1:9335/?shell[0]=0&pwn[1]=0```

![](/SHELLCTF/pic/Collision_2.png)


- Flag : ```SHELL{1nj3ct_&_coll1d3_9d25f1cfdeb38a404b6e8584bec7a319}```

#### Reference 

- [CTFTime Write up](https://ctftime.org/task/12375)
- [(Reading) The SHA256 Collision That Wasn’t ](https://blog.cotten.io/the-sha256-collision-that-wasnt-82714fb1413f)
- [(Reading)新碰撞攻击无情鞭尸SHA1算法，使用SHA256的BTC在瑟瑟发抖？](https://www.8btc.com/article/543858)
- [(Reading)SHA1 Collision Site : Shattered](https://shattered.io/)
- [(Reading)九百萬兆次演算實現碰撞！Google 攻破了最重要的加密技術](https://www.inside.com.tw/article/8614-google-just-had-first-sha-1-collision)
- [(Reading)Paper For SHA1 Collision](https://shattered.io/static/shattered.pdf)
- [(Tools)Crack SHA256](https://cyber-99.co.uk/mesmerize/thm-crack-the-hash-ctf)
- [(Tools Introduce)THM – Crack The Hash CTF](https://cyber-99.co.uk/mesmerize/thm-crack-the-hash-ctf)

#### To Do List 

- 理解該提原理, 為何payload 會產生 sha256 collision
- Reasearch About SHA256 Collision


<h3 id='FunWithToken'> Fun With Token </h3>

Link of Problem : http://3.142.122.1:9334/

![](/SHELLCTF/pic/FunWithToken_1.png)


- Two Link in main page 
    ![](/SHELLCTF/pic/FunWithToken_2.png)
    1. Admins (/adminNames) 
    2. Login (/login)

- Admins link detail process
    1. Will Download a file 
    ![](/SHELLCTF/pic/FunWithToken_3.png)
    ![](/SHELLCTF/pic/FunWithToken_4.png)
    2. The File Content 
    ![](/SHELLCTF/pic/FunWithToken_5.png)
    3. Interpre with this request(/adminNames) in detail 
        a. Access /adminNames
        b. Redirect to (/getFile?file=admins)
        ![](/SHELLCTF/pic/FunWithToken_6.png)
        ![](/SHELLCTF/pic/FunWithToken_7.png)

    4. According to the subject , This web has known vulnerability
    5. I guess the vulnerability will happen on the  download page URL which URL is ```3.142.122.1:9334/getFile?file=admins``` 
    6. If we give an unexist file , the error like the picture 
    ![](/SHELLCTF/pic/FunWithToken_8.png)
    7. So, we need to know what's the file we want to find
    8. BTW, the file parameter have size limitation 
    ![](/SHELLCTF/pic/FunWithToken_9.png)

- Let's back to the main page and read the web source, We got something interesting , it's two hint.
    ![](/SHELLCTF/pic/FunWithToken_10.png)
    1. First one is talk about that there is a admin page (/admin)
    2. Second one is talk about the secret is store in environment

-  With the error message we get in previously , we know the backend server may PHP and the framework is Laravel(If you google /app/public will know this seems is a default directory for PHP Laravel)
![](/SHELLCTF/pic/FunWithToken_11.png)
    - [Reference](https://laravel.com/docs/8.x/structure)

- In the Laravel Official Page has mentioned that the environment file is ```.env```
![](/SHELLCTF/pic/FunWithToken_12.png)

- So, let's try to find the ```.env``` in the default directory , and we find the file is in ```/app/.env``` by this payload(```../.env```)
![](/SHELLCTF/pic/FunWithToken_13.png)
![](/SHELLCTF/pic/FunWithToken_14.png)

- Now we have adminNames file with **admin name(0xd4127c3c/din_djarin11)** and the secret file with **secret value(secret=G00D_s0ld13rs_k33p_s3cret5)** .
- Then Next Step , let's talk about login , we send login request to burp(The password is not the point in here , so we just gave an any string) , and we can find the response header will have a token 
![](/SHELLCTF/pic/FunWithToken_15.png)
![](/SHELLCTF/pic/FunWithToken_16.png)
![](/SHELLCTF/pic/FunWithToken_17.png)
- Now, just remeber this token 
```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InF2YV9xd25ldmExMSIsInBhc3N3b3JkIjoiMzU1Nzk4MTI0NCIsImFkbWluIjoiZ2VociIsImlhdCI6MTYyMzAzODcxOX0.QNmzkFS899SweMKQEeaU0ayrVzQ159gXnZQzzvuRLpM
```

- We try to access the /admin which is mentioned in the web source
- we got the following message : 
    - ``` "Maybe send the token via Headers ... for Authorization?"```
    ![](/SHELLCTF/pic/FunWithToken_18.png)
    - If we send the /admin to burp and add the Authorization in request header with the token we just get, we will get the message : ``` You are not an Admin```
    ![](/SHELLCTF/pic/FunWithToken_19.png)

- So, I think the problem is on the token now .

- We copy the token to [jwt decode page](https://jwt.io/), and get the following message  
![](/SHELLCTF/pic/FunWithToken_20.png)
- Compare to our request , we can find some interesting thing
    ![](/SHELLCTF/pic/FunWithToken_21.png)
    1. The username and password seem be encrypted in token 
    2. Here is a admin with a stange value 

- Then we first find the encryption algorithm in token value is [ROT13](https://rot13.com/) 
![](/SHELLCTF/pic/FunWithToken_22.png)

- With this message , we know the admin value is 'false'
![](/SHELLCTF/pic/FunWithToken_23.png)

- So maybe we just need to change the value of admin to true and envrypted it with ROT13 then re-generate a new token with the secret value in the Verify Signature part in jwt.io 
![](/SHELLCTF/pic/FunWithToken_24.png)

- We send the request to /admin with new token , then we get another strange string .
![](/SHELLCTF/pic/FunWithToken_25.png)
![](/SHELLCTF/pic/FunWithToken_26.png)

- Let's decrypt it with ROT13 , and we get the flag 
![](/SHELLCTF/pic/FunWithToken_27.png)

Get The Flag : SHELL{T0k3ns_d0_m4tt3r_4e91af4506f384d460f0f0c6e9e5fe4a}


<h3 id='login'>Login</h3>

- [Login Page](/SHELLCTF/Web/Login/index)

![](/SHELLCTF/pic/Login_1)

- View Web Source, and there is a [main.js](/SHELLCTF/Web/Login/main.js) will be call

![](/SHELLCTF/pic/Login_2)

- Let's see this JS file in Source Panel 
- In the top of ```main.js``` file ,  it's a code snippet ise to check the user and password 
- From that code snippet , we can know 
    1. user is : ```din_djarin11```
    2. password is : ```9ef71a8cd681a813cfd377817e9a08e5```
![](/SHELLCTF/pic/Login_3)

- For Password part , it seems to be hash , let's try to decrypt it with [tools](https://cyber-99.co.uk/mesmerize/thm-crack-the-hash-ctf)
- Get the password : ir0nm4n

![](/SHELLCTF/pic/Login_4)

- Let's login , then we'll get a text file 
- The Flag is in this file 

![](/SHELLCTF/pic/Login_5)

![](/SHELLCTF/pic/Login_6)


- Get Flag : SHELL{th1s_i5_th3_wa7_845ad42f4480104b698c1e168d29b739}

![](/SHELLCTF/pic/Login_7)






#### Reference 
- [(Tool)JWT.io](https://jwt.io/)
- [(Tool)ROT13](https://rot13.com/)
- [(Reading)Authorization Header](https://www.loginradius.com/blog/async/everything-you-want-to-know-about-authorization-headers/)
- [(Reading)Laravel Configuration](https://laravel.com/docs/8.x/configuration)





###### tags: `CTF` `ShellCTF 2021` `Security`