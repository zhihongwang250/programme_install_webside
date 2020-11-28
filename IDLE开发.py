# coding:utf-8

'''designed IDLE python script editor
       开发IDLE Python文字编辑器'''

from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
import sys
import os
import requests # 网络爬虫分析，用来检测版本

def openfile():
    openfilename = askopenfilename()
    if openfilename == '':
        return
    with open(openfilename) as file:
        text_edit.insert(1.0, END)
        mainwindow.title(openfilename + '中文版IDLE文件打开')
        file.close()

def newfile():
    text_edit.delete(1.0, END)
    mainwindow.title('中文版IDLE')

def savefile():
    savefilename = asksaveasfilename()
    if savefilename == '':
        return
    with open(savefilename) as file:
        file.write(text_edit.get(1.0,END))
        file.close()

def open_module():
    pass

def undo():
    pass

def redo():
    pass

def cut():
    pass

def copy():
    pass

def paste():
    pass

def sAll():
    pass

def helping():
    pass

def about_soft():
    showinfo('关于中文版IDLE', '中文版IDLE\n版本1.1\n版权所有')

def update():
    try:
        update_date = requests.get('https://zhihongwang250.github.io/programme_install_webside')
        if update_date.status_code == requests.codes.ok:
            if 'vsrsion=1.0' in update_date:
                askquestion('安装更新', '检测到了新版本，是否更新？')
            else:
                showinfo('安装更新', '已经是最新版本')
        else:
            showerror('安装更新', '网络异常或连接失败')
    except:
        showerror('安装更新', '无法正常安装更新')

def close():
    sys.exit()

mainwindow = Tk()
mainwindow.title('中文版IDLE')

mainmenu = Menu(mainwindow)
file = Menu(mainmenu, tearoff = 0)
edit  = Menu(mainmenu, tearoff = 0)
about = Menu(mainwindow, tearoff = 0)

# 文件编辑菜单
mainmenu.add_cascade(label = '文件', menu = file)
file.add_command(label =  '新建文件', command = newfile)
file.add_command(label = '打开文件', command = openfile)
file.add_command(label = '保存文件', command = savefile)
file.add_command(label = '打开Python代码库', command  = open_module)
file.add_separator()
file.add_command(label = '关闭', command = close)
file.add_command(label = '退出', command = close)
mainwindow.config(menu = mainmenu)

# 编辑编辑菜单
mainmenu.add_cascade(label = '编辑',menu = edit)
edit.add_command(label = '撤销', command = undo)
edit.add_command(label = '重做', command = redo)
edit.add_separator()
edit.add_command(label = '剪切', command = cut)
edit.add_command(label = '复制', command = copy)
edit.add_command(label = '粘贴', command = paste)
edit.add_command(label = '全选', command = sAll)
mainwindow.config(menu = mainmenu)

mainmenu.add_cascade(label = '帮助', menu = about)
about.add_command(label = '查看帮助', command = help)
about.add_separator()
about.add_command(label = '关于中文版IDLE', command = about_soft)
about.add_command(label = '检查更新', command = update)
mainwindow.config(menu = mainmenu)

Label(mainwindow, text = '在文本编辑区域向下滑动鼠标滚轮来查看文件').pack()
text_edit = Text(mainwindow)
text_edit.pack()

# 启动事件主循环
mainwindow.mainloop()
