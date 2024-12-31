# os.stat() 与 stat

## os.stat
os.stat("文件路径")，用来返回指定文件的文件系统属性信息

    import os
    print(os.stat("/root/python/zip.py"))
Console: os.stat_result(st_mode=33206, st_ino=1407374883773760, st_dev=272305337, st_nlink=1, st_uid=0, st_gid=0, st_size=30646,<br>
st_atime=1701827453, st_mtime=1699341164, st_ctime=1701824990)
```
os.stat("/root/python/zip.py").st_mode # 权限模式<br>
os.stat("/root/python/zip.py").st_ino  # inode number<br>
os.stat().set_dev: device<br>
os.stat().st_nlink: number of hard links<br>
os.stat().st_uid: 所有用户的user id<br>
os.stat().st_gid: 所有用户的group id<br>
os.stat().st_size: 文件的大小，以位为单位<br>
os.stat().st_atime: 文件最后的访问时间<br>
os.stat().st_mtime: 文件最后的修改时间<br>
os.stat().st_ctime: 文件创建时间<br>
```
## stat
1. 可对os.stat().st_mode 进行一些判断；例如：stat.S_ISREG(mode) 判断是否一般文件
    - S_ISLINK 是否链接文件
    - S_ISSOCK 是否套接字文件
    - S_ISFIFO 是否命名管道
    - S_ISBLK  是否块设备
    - S_ISCHR  是否字符设备
    - S_ISDIR  是否目录
    - S_IMODE  返回文件权限的chmod格式
2. os.chmod权限设置使用<br>
    stat标识符说明：
    |标识符|说明|
    |---|---|
    |stat.S_IREAD|Read by owner对于拥有者读的权限|
    |stat.S_IWRITE|Write by owner对于拥有者写的权限|
    |stat.S_IEXEC|Execute by owner对于拥有者执行的权限|
    |stat.S_IRWXU|Read,write,and execute by owner对于拥有者读写执行的权限|
    |stat.S_IRUSR|Read by owner对于拥有者读的权限|
    |stat.S_IWUSR|Write by owner对于拥有者写的权限|
    |stat.S_IXUSR|Execute by owner对于拥有者执行的权限|
    |stat.S_IRWXG|Read,write,and execute by group对于同组的人读写执行的权限|
    |stat.S_IRGRP|Read by group对于同组读的权限|
    |stat.S_IWGRP|Write by group对于同组写的权限|
    |stat.S_IXGRP|Execute by group对于同组执行的权限|
    |stat.S_IRWXO|Read,write,and execute by others对于其他组读写执行的权限|
    |stat.S_IROTH|Read by others对于其他组读的权限|
    |stat.S_IWOTH|Write by others对于其他组写的权限|
    |stat.S_IXOTH|Execute by others对于其他组执行的权限|
    |stat.S_ISVTX|Save text image after execution在执行之后保存文字和图片|