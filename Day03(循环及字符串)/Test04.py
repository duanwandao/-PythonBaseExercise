"""
*
***
*****
*******

    *        i = 0    4
   ***       i = 1    3
  *****      i = 2    2
 *******     i = 3    1
  *****
   ***
    *


"""
line = 4
for i in range(0,line):
    # 打印每一行中的" "
    for k in range(line-i):
        print("-", end="")
    #打印每一行中"*"
    for j in range(2*i+1):
        print("*",end="")

    print()
# for i in range(0,line).__reversed__():
#     # 打印每一行中的" "
#     for k in range(line-i):
#         print("-", end="")
#     #打印每一行中"*"
#     for j in range(2*i+1):
#         print("*",end="")
#
#     print()
