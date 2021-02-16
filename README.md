# deepin-wine5 安装打包器

#### 介绍
一个方便使用的 deepin-wine5 应用打包器，可以联合我开发的 deepin-wine 运行器使用
使用 Python3 的 tkinter 构建
（测试平台：deepin 20.1 1030）
程序创建的 deb 构建临时文件夹目录树：
```
/XXX
├── DEBIAN
│   └── control
└── opt
└── apps
    └── XXX
        ├── entries
        │   ├── applications
        │   │   └── XXX.desktop
        │   └── icons
        │       └── hicolor
        │           └── scalable
        │               └── apps
        │                   └── XXX.png（XXX.svg）
        ├── files
        │   ├── files.7z
        │   └── run.sh
        └── info

11 directories, 6 files
```
对比自己开发的上一个软件（spark-webapp-runtime 运行器），控件的布局方法有变化，从 pack() 到 grid()

#### 软件架构
i386 和 amd64，deepin-wine5 运行在哪就运行在哪


#### 源码安装教程

1.  安装所需依赖

```
sudo apt install python3 python3-tk git
```

2.  下载本程序

```
git clone https://gitee.com/gfdgd-xi/deep-wine5-application-packer.git
```

3.  运行本程序

```
cd deep-wine5-application-packer
chmod 777 main.py
./main.py
```


#### 使用说明

提示：
1、deb 打包软件包名要求：
软件包名只能含有小写字母(a-z)、数字(0-9)、加号(+)和减号(-)、以及点号(.)，软件包名最短长度两个字符；它必须以字母开头
2、如果要填写路径，有“浏览……”按钮的是要填本计算机对应文件的路径，否则就是填写安装到其他计算机使用的路径
3、输入 deepin-wine5 的容器路径时最后面请不要输入“/”
4、输入可执行文件的运行路径时是以“C:/XXX/XXX.exe”的格式进行输入，默认是以 C： 为开头，不用“\”做命令的分隔，而是用“/”
5、.desktop 的图标只支持 PNG 格式和 SVG 格式，其他格式无法显示图标


#### 特技

（吹一点）
1、调用了系统命令（7z、dpkg）
2、……
3、……
