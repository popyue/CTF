# Subsi


- Cipher :  ```HITSS{5X65Z1ZXZ10F_E1LI3J}```

- [Script.py](/SHELLCTF/Crypto/Subsi/script.py)

- Based on the name we can assume it might a substitution cipher

```
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ{}_1234567890'
key   = 'QWERTPOIUYASDFGLKJHZXCVMNB{}_1234567890'

text = <flag>

def encrypter(text,key):
    encrypted_msg = ''
    for i in text:
        index = alpha.index(i)
        encrypted_msg += key[index]
    # print(encrypted_msg)
    return encrypted_msg

```

### Solution 

- [script_solve.py](/SHELLCTF/Crypto/Subsi/script_solve.py)

```
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
```

- Get Flag : SHELL{5U65T1TUT10N_C1PH3R} 