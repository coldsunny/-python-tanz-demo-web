#-*-coding:utf-8-*-
__author__ = 'Administrator'

'''for x in range(4):
    print(x)'''
'''a,b = 0,1
while b<10:
    print(b)
    a,b = b,a+b
print(type(a))'''

'''#交换变量
a=2
b=3
a,b=b,a
print a,b

#if语句在行内
print 'Hello' if True else 'World'

#连接
kf=['tom',45]
nf=['sawyer',33]
print kf+nf

print str(1)+'world'
print '1'+'world'
print 1,'world'
print kf,1

print .3/.1

True == False
if True:
    print 'hello'
else:
    print 'world' '''

#遍历目录方法
import os
filelist = []
rootdir ="F:/"
for root,subFolders,files in os.walk(rootdir):
    if '.svn' in subFolders:
        subFolders.remove('.svn')# 排除特定目录
    for file in files:
        if file.find(".t2t") \   #"\"可以换行
                != -1:# 查找特定扩展名的文件
            file_dir_path = os.path.join(root,file)
            filelist.append(file_dir_path)
print filelist





