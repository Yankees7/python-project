# pipenv的快速入门
解决部署服务，从一个环境到另一个环境，第三方库的众多包又要重新安装。
解决pyinstaller每次打包很大，打了许多不用的包；现在做到精准性打包。

pipenv提供类似maven，npm等功能的依赖包管理器

总之，pipenv可以帮助我们管理python和第三方库的版本。

## 0 快速上手
1. cmd中输入命令 pip install pipenv 安装pipenv
2. cmd切换路径到需要建立虚拟环境的项目目录下
3. 初始化特定版本的环境pipenv --python 3.6 (可选，如果不初始，则跟随系统默认：)
4. 输入命令 pipenv install 开始安装虚拟环境
5. 安装完毕后输入命令 pipenv shell 进入虚拟环境
6. pipenv install xxx 安装相关依赖包
7. pipenv graph 查看目前按照的依赖包

--python TEXT 指定python解释器（不执行会采取默认，选择其他版本号3.7等必须在环境变量里面，不在环境变量里面则指定完整路径）

## 1.安装 
pip install pipenv

## 2.卸载
pip uninstall pipenv

## 3.更新
pipinstall --user --upgrade pipenv

## 4.首次运行
pipenv install

### 4.1 Pipfile 和 Pipfile.lock
第一次在项目中运行pipenv命令，会创建一个名为Pipfile的文件。
如果运行install、update等命令的话，除了创建，还会创建一个Pipfile.lock文件，类似npm中的lock文件。
这两个文文件随着相关命令自动更新

Pipfile: 用于保存项目的python版本、依赖包等相关信息
Pipfile.lock: 用于对Pipfil的锁定

## 5.删除虚拟环境
pipenv --rm

## 6.与虚拟环境相关的常用命令
**pipenv install**:
- 若项目目录中虚拟环境未创建且无Pipfile文件，将按照虚拟环境并创建Pipfile文件
- 若项目目录中虚拟环境未创建且有Pipfile文件，将根据Pipfile文件来安装相应python版本和依赖包
- 若项目目录中虚拟环境已创建且有Pipfile文件，将根据Pipfile文件来安装依赖包







