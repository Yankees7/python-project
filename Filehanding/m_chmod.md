# os.chmod模块说明

os.chmod(path, mode)

**mode说明**：<br>
**0o开头表示八进制**
    1. 可填十进制数字。例如：256 （对应权限位0o400）
    2. 可填八进制数字。例如：Oo777(对应权限位0o777)
    3. 可填stat falgs。例如：stat.S_IRUSR（拥有者具有读权限Oo400）


```python
import os
os.chmod("/tmp/foo.txt", stat.S_IXGRP) # 用户组具有执行权限
```