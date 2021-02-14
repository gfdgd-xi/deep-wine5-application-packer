#!/usr/bin/env python3
#########################################################################
# 作者：gfdgd xi
# 版本：1.0.0
# 感谢：感谢 deepin-wine 团队，提供了 deepin-wine 给大家使用，让我能做这个程序
# 基于 Python3 的 tkinter 构建
#########################################################################
#################
# 引入所需的库
#################
import tkinter as tk
import tkinter.messagebox as messagebox
import tkinter.filedialog as filedialog
import threading
import traceback
import shutil
import os

def button1_cl():
    path = filedialog.askdirectory(title="选择 deepin-wine5 容器", initialdir="~/.deepinwine")
    if path != "":
        e6_text.set(path)

def button2_cl():
    path = filedialog.askopenfilename(filetypes=[("PNG图标", "*.png"), ("SVG图标", "*.svg"), ("全部文件", "*.*")], title="选择图标文件", initialdir="~")
    if path != "":
        e9_text.set(path)

def button3_cl():
    path = filedialog.askdirectory(title="选择临时路径", initialdir="~")
    if path != "":
        e11_text.set(path)

def button4_cl():
    path = filedialog.asksaveasfilename(filetypes=[("deb 文件", "*.deb"), ("所有文件", "*.*")], title="保存 deb 包", initialdir="~", initialfile="{}_{}_i386.deb".format(e1_text.get(), e2_text.get()))
    if path != "":
        e12_text.set(path)

def disabled_or_NORMAL_all(choose):
    chooses = {True: tk.NORMAL, False: tk.DISABLED}
    a = chooses[choose]
    label1.configure(state=a)
    label2.configure(state=a)
    label3.configure(state=a)
    label4.configure(state=a)
    label5.configure(state=a)
    label6.configure(state=a)
    label7.configure(state=a)
    label8.configure(state=a)
    label9.configure(state=a)
    label10.configure(state=a)
    label11.configure(state=a)
    label12.configure(state=a)
    label14.configure(state=a)
    label15.configure(state=a)
    e1.configure(state=a)
    e2.configure(state=a)
    e3.configure(state=a)
    e4.configure(state=a)
    e5.configure(state=a)
    e6.configure(state=a)
    e7.configure(state=a)
    e8.configure(state=a)
    e9.configure(state=a)
    e10.configure(state=a)
    e11.configure(state=a)
    e12.configure(state=a)
    e15.configure(state=a)
    button1.config(state=a)
    button2.config(state=a)
    button3.config(state=a)
    button4.config(state=a)
    button5.config(state=a)
    option1.config(state=a)

def make_deb():
    clean_textbox1_things()
    disabled_or_NORMAL_all(False)
    if e1_text.get() == "" or e2_text.get() == "" or e3_text.get() == "" or e4_text.get() == "" or e5_text.get() == "" or e6_text.get() == "" or e7_text.get() == "" or e8_text.get() == "" or e11_text.get() == "" or e12_text.get() == "" or e15_text.get() == "":
        messagebox.showinfo(title="提示", message="必填信息没有填写完整，无法继续构建 deb 包")
        disabled_or_NORMAL_all(True)
        label13_text_change("必填信息没有填写完整，无法继续构建 deb 包")
        return
    thread = threading.Thread(target=make_deb_threading)
    thread.start()

def label13_text_change(thing):
    label13_text.set("当前 deb 打包情况：{}".format(thing))

def make_deb_threading():
    try:
        label13_text_change("正在检查文件是否存在并为后面步骤准备……")
        a = ""
        if e6_text.get() == "/":
            b = e6_text.get()[:-1]
        else:
            b = e6.get()
        if e9_text.get() != "":
            a = "/opt/apps/{}/entries/icons/hicolor/scalable/apps/{}.svg".format(e1_text.get(), e1_text.get())
            if not os.path.exists(e9_text.get()):
                messagebox.showerror(title="提示", message="图标的路径填写错误，无法进行构建 deb 包")
                disabled_or_NORMAL_all(True)
                label13_text_change("图标的路径填写错误，无法进行构建 deb 包")
                return
        if not os.path.exists(e6_text.get()) or not os.path.exists(e11_text.get()):
            messagebox.showerror(title="提示", message="路径填写错误，无法继续构建 deb 包")
            disabled_or_NORMAL_all(True)
            label13_text_change("图标的路径填写错误，无法进行构建 deb 包")
            return
        label13_text_change("正在删除对构建 deb 包有影响的文件……")
        if os.path.exists("{}/DEBIAN".format(e11_text.get())):
            shutil.rmtree("{}/DEBIAN".format(e11_text.get()))
        if os.path.exists("{}/opt".format(e11_text.get())):
            shutil.rmtree("{}/opt".format(e11_text.get()))
        label13_text_change("正在创建目录……")
        os.makedirs("{}/DEBIAN".format(e11_text.get()))
        os.makedirs("{}/opt/apps/{}/entries/applications".format(e11_text.get(), e1_text.get()))
        os.makedirs("{}/opt/apps/{}/entries/icons/hicolor/scalable/apps".format(e11_text.get(), e1_text.get()))
        os.makedirs("{}/opt/apps/{}/files".format(e11_text.get(), e1_text.get()))
        label13_text_change("正在创建文件……")
        os.mknod("{}/DEBIAN/control".format(e11_text.get()))
        os.mknod("{}/opt/apps/{}/entries/applications/{}.desktop".format(e11_text.get(), e1_text.get(), e1_text.get()))
        os.mknod("{}/opt/apps/{}/files/run.sh".format(e11_text.get(), e1_text.get()))
        os.mknod("{}/opt/apps/{}/info".format(e11_text.get(), e1_text.get()))
        label13_text_change("正在打包 deepin-wine5 容器")
        run_command("7z a {}/opt/apps/{}/files/files.7z {}/*".format(e11_text.get(), e1_text.get(), b))
        label13_text_change("正在复制文件……")
        if e9_text.get() != "":
            shutil.copy(e9_text.get(), "{}/opt/apps/{}/entries/icons/hicolor/scalable/apps/{}.svg".format(e11_text.get(), e1_text.get(), e1_text.get()))
        label13_text_change("正在计算文件大小……")
        size = getFileFolderSize(e11_text.get()) / 1024
        label13_text_change("正在写入文件……")
        write_txt("{}/DEBIAN/control".format(e11_text.get()), 'Package: {}\nVersion: {}\nArchitecture: i386\nMaintainer: {}\nDepends: deepin-wine5:i386 (>= 5.0.4-1), deepin-wine5-i386 (>= 5.0.4-1), deepin-wine-helper:i386 (>= 5.1.1-1)\nConflicts: {}\nReplaces: {}\nProvides: {}\nSection: non-free/otherosfs\nPriority: optional\nMulti-Arch: foreign\nDescription: {}\nInstalled-Size: {}\n'.format(e1_text.get(), e2_text.get(), e4_text.get(), e1_text.get(), e1_text.get(), e1_text.get(), e3_text.get(), str(size)))
        write_txt("{}/opt/apps/{}/entries/applications/{}.desktop".format(e11_text.get(), e1_text.get(), e1_text.get()), '#!/usr/bin/env xdg-open\n[Desktop Entry]\nEncoding=UTF-8\nType=Application\nX-Created-By={}\nCategories={};\nIcon={}\nExec="/opt/apps/{}/files/run.sh" {}\nName={}\nComment={}\nMimeType={}'.format(e4_text.get(), option1_text.get(), a, e1_text.get(), e15_text.get(), e8_text.get(), e3_text.get(), e10_text.get()))
        write_txt("{}/opt/apps/{}/files/run.sh".format(e11_text.get(), e1_text.get()), '''#!/bin/sh\n\n#   Copyright (C) 2020 Deepin, Inc.\n\nBOTTLENAME="{}"\nAPPVER="{}"\nEXEC_PATH="{}"\nSTART_SHELL_PATH="/opt/deepinwine/tools/run_v3.sh"\n\nexport MIME_TYPE=""\nexport DEB_PACKAGE_NAME="{}"\nexport APPRUN_CMD="deepin-wine5"\n\nif [ -n "$EXEC_PATH" ];then\n        $START_SHELL_PATH $BOTTLENAME $APPVER "$EXEC_PATH" "$@"\n    else\n        $START_SHELL_PATH $BOTTLENAME $APPVER "uninstaller.exe" "$@"\nfi'''.format(e5_text.get(), e2_text.get(), e7_text.get(), e1_text.get()))
        write_txt("{}/opt/apps/{}/info".format(e11_text.get(), e1_text.get()), '{\n    "appid": "' + e1_text.get() + '",\n    "name": "' + e8_text.get() + '",\n    "version": "' + e2_text.get() + '",\n    "arch": ["i386"],\n    "permissions": {\n        "autostart": false,\n        "notification": false,\n        "trayicon": true,\n        "clipboard": true,\n        "account": false,\n        "bluetooth": false,\n        "camera": false,\n        "audio_record": false,\n        "installed_apps": false\n    }\n}')
        label13_text_change("正在修改文件权限……")
        run_command("chmod 644 {}/opt/apps/{}/files/run.sh".format(e11_text.get(), e1_text.get()))
        run_command("chmod 644 {}/opt/apps/{}/info".format(e11_text.get(), e1_text.get()))
        run_command("chmod 755 {}/opt/apps/{}/files/run.sh".format(e11_text.get(), e1_text.get()))
        run_command("chmod 644 {}/opt/apps/{}/entries/applications/{}.desktop".format(e11_text.get(), e1_text.get(), e1_text.get()))
        label13_text_change("正在构建 deb 包……")
        run_command("dpkg -b {} {}".format(e11_text.get(), e12_text.get()))
        label13_text_change("完成构建！")
        disabled_or_NORMAL_all(True)
    except Exception as e:
        messagebox.showerror(title="错误", message="程序出现错误，错误信息：\n{}".format(traceback.format_exc()))
        traceback.print_exc()
        label13_text_change("deb 包构建出现错误：{}".format(repr(e)))
        chang_textbox1_things(traceback.format_exc())
        disabled_or_NORMAL_all(True)

# 写入文本文档
def write_txt(path, things):
    file = open(path, 'a+', encoding='UTF-8')  # 设置文件对象
    file.write(things)  # 写入文本
    file.close()  # 关闭文本对象

def chang_textbox1_things(things):
    textbox1.configure(state=tk.NORMAL)
    textbox1.insert('end', things)
    textbox1.configure(state=tk.DISABLED)

def clean_textbox1_things():
    textbox1.configure(state=tk.NORMAL)
    textbox1.delete('1.0','end')
    textbox1.configure(state=tk.DISABLED)

def run_command(command):
    result = os.popen(command)
    res = result.read()
    for line in res.splitlines():
        chang_textbox1_things(line + "\n")


def getFileFolderSize(fileOrFolderPath):
    """get size for file or folder"""
    totalSize = 0
    if not os.path.exists(fileOrFolderPath):
        return totalSize
    if os.path.isfile(fileOrFolderPath):
        totalSize = os.path.getsize(fileOrFolderPath)  # 5041481
        return totalSize
    if os.path.isdir(fileOrFolderPath):
        with os.scandir(fileOrFolderPath) as dirEntryList:
            for curSubEntry in dirEntryList:
                curSubEntryFullPath = os.path.join(fileOrFolderPath, curSubEntry.name)
                if curSubEntry.is_dir():
                    curSubFolderSize = getFileFolderSize(curSubEntryFullPath)  # 5800007
                    totalSize += curSubFolderSize
                elif curSubEntry.is_file():
                    curSubFileSize = os.path.getsize(curSubEntryFullPath)  # 1891
                    totalSize += curSubFileSize
            return totalSize

# 显示“关于这个程序”窗口
def about_this_program():
    messagebox.showinfo(title="关于这个程序", message="一个基于 Python3 的 tkinter 制作的 deepin-wine5 应用打包器\n版本：1.0\n适用平台：Linux\ntkinter 版本：" + str(tk.TkVersion))

# 显示“提示”窗口
def helps():
    messagebox.showinfo(title="提示", message="提示：\n1、deb 打包软件包名要求：\n软件包名只能含有小写字母(a-z)、数字(0-9)、加号(+)和减号(-)、以及点号(.)，软件包名最短长度两个字符；它必须以字母开头\n2、如果要填写路径，有“浏览……”按钮的是要填本计算机对应文件的路径，否则就是填写安装到其他计算机使用的路径\n3、输入 deepin-wine5 的容器路径时最后面请不要输入“/”\n4、输入可执行文件的运行路径时是以“C:/XXX/XXX.exe”的格式进行输入，默认是以 C： 为开头，不用“\”做命令的分隔，而是用“/”")

###############
#
###############
window = tk.Tk()
window.title("deepin-wine5 应用打包器")
e1_text = tk.StringVar()
e2_text = tk.StringVar()
e3_text = tk.StringVar()
e4_text = tk.StringVar()
e5_text = tk.StringVar()
e6_text = tk.StringVar()
e7_text = tk.StringVar()
e8_text = tk.StringVar()
e9_text = tk.StringVar()
e10_text = tk.StringVar()
e11_text = tk.StringVar()
e12_text = tk.StringVar()
e15_text = tk.StringVar()
label13_text = tk.StringVar()
option1_text = tk.StringVar()
option1_text.set("Network")
label13_text.set("当前 deb 打包情况：暂未打包")
label1 = tk.Label(window, text="要打包的 deb 包的包名（*必填）")
label2 = tk.Label(window, text="要打包的 deb 包的版本号（*必填）")
label3 = tk.Label(window, text="要打包的 deb 包的说明（*必填）")
label4 = tk.Label(window, text="要打包的 deb 包的维护者（*必填）")
label5 = tk.Label(window, text="要解压的 deepin-wine5 容器的容器名（*必填）")
label6 = tk.Label(window, text="要解压的 deepin-wine5 容器（*必填）")
label7 = tk.Label(window, text="要解压的 deepin-wine5 容器里需要运行的可执行文件路径（*必填）")
label8 = tk.Label(window, text="要显示的 .desktop 文件的名称（*必填）")
label9 = tk.Label(window, text="要显示的 .desktop 文件的图标（选填）")
label10 = tk.Label(window, text="要显示的 .desktop 文件的 MimeType 内容（选填）")
label11 = tk.Label(window, text="打包 deb 时的临时路径（尽可能大）（*必填）")
label12 = tk.Label(window, text="打包 deb 的保存路径（*必填）")
label13 = tk.Label(window, textvariable=label13_text)
label14 = tk.Label(window, text="要显示的 .desktop 文件的分类（*必填）")
label15 = tk.Label(window,text="要解压的 deepin-wine5 容器里需要运行的可执行文件的参数（选填）")
e1 = tk.Entry(window, textvariable=e1_text, width=100)
e2 = tk.Entry(window, textvariable=e2_text, width=100)
e3 = tk.Entry(window, textvariable=e3_text, width=100)
e4 = tk.Entry(window, textvariable=e4_text, width=100)
e5 = tk.Entry(window, textvariable=e5_text, width=100)
e6 = tk.Entry(window, textvariable=e6_text, width=100)
e7 = tk.Entry(window, textvariable=e7_text, width=100)
e8 = tk.Entry(window, textvariable=e8_text, width=100)
e9 = tk.Entry(window, textvariable=e9_text, width=100)
e10 = tk.Entry(window, textvariable=e10_text, width=100)
e11 = tk.Entry(window, textvariable=e11_text, width=100)
e12 = tk.Entry(window, textvariable=e12_text, width=100)
e15 = tk.Entry(window, textvariable=e15_text, width=100)
button1 = tk.Button(window, text="浏览……", command=button1_cl)
button2 = tk.Button(window, text="浏览……", command=button2_cl)
button3 = tk.Button(window, text="浏览……", command=button3_cl)
button4 = tk.Button(window, text="浏览……", command=button4_cl)
button5 = tk.Button(window, text="打包……", command=make_deb)
option1 = tk.OptionMenu(window, option1_text, "Network", "Chat", "Audio", "Video", "Graphics", "Office", "Translation", "Development", "Utility")
textbox1 = tk.Text(window, width=100, height=4)
textbox1.configure(state=tk.DISABLED)
menu = tk.Menu(window) # 设置菜单栏
programmenu = tk.Menu(menu,tearoff=0) # 设置“程序”菜单栏
menu.add_cascade(label="程序",menu=programmenu)
programmenu.add_command(label="退出程序",command=window.quit) # 设置“退出程序”项
help = tk.Menu(menu,tearoff=0) # 设置“帮助”菜单栏
menu.add_cascade(label="帮助",menu=help)
help.add_command(label="小提示",command=helps) # 设置“小提示”项
help.add_separator() # 设置分界线
help.add_command(label="关于这个程序",command=about_this_program) # 设置“关于这个程序”项
# 添加控件
window.config(menu=menu) # 显示菜单栏
label1.grid(row=0, column=0)
e1.grid(row=0, column=1)
label2.grid(row=1, column=0)
e2.grid(row=1, column=1)
label3.grid(row=2, column=0)
e3.grid(row=2, column=1)
label4.grid(row=3, column=0)
e4.grid(row=3, column=1)
label5.grid(row=4, column=0)
e5.grid(row=4, column=1)
label6.grid(row=5, column=0)
e6.grid(row=5, column=1)
button1.grid(row=5, column=2)
label7.grid(row=6, column=0)
e7.grid(row=6, column=1)
label14.grid(row=7, column=0)
option1.grid(row=7, column=1)
label15.grid(row=8, column=0)
e15.grid(row=8, column=1)
label8.grid(row=9, column=0)
e8.grid(row=9, column=1)
label9.grid(row=10, column=0)
e9.grid(row=10, column=1)
button2.grid(row=10, column=2)
label10.grid(row=11, column=0)
e10.grid(row=11, column=1)
label11.grid(row=12, column=0)
e11.grid(row=12, column=1)
button3.grid(row=12, column=2)
label12.grid(row=13, column=0)
e12.grid(row=13, column=1)
button4.grid(row=13, column=2)
button5.grid(row=14, column=1)
label13.grid(row=15, column=1)
textbox1.grid(row=16, column=1)
window.mainloop()
