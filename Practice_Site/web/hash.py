# -*- coding: utf-8 -*-

import hashlib

filename="shell.php"
m=hashlib.md5()
s=hashlib.sha1()
# 讀取檔案內容，計算 MD5 雜湊值
with open(filename, "rb") as f:
  buf = f.read()
  m.update(buf)

h = m.hexdigest()
print(h)
s.update(h)
n=s.hexdigest()
print(n)
