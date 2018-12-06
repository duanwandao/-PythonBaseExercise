"""
批量修改文件名：
    1.找到所有文件
    2.修改文件名

"""
# import 001
import os

oldName = '001.py'
newName = 'sxt'+oldName
os.rename(oldName,newName)