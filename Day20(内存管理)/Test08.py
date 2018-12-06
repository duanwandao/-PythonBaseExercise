"""
md5的加密原理（不可逆性）

e10adc3949ba59abbe56e057f20f883e
ae96df4c5a919edc789939c388033d52
"""
from hashlib import *
m = md5()
account = '13388888888'
# pw = '123456'
pw = "Cbtbtptpbcptdtptp_1234_aaa"
# 使用md5方式加密
m.update(pw.encode())
# 打印加密后的结果
print(m.hexdigest())