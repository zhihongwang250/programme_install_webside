# _ * _ coding:utf-8 _ * _

'''designed IDLE python script editor
       开发IDLE Python文字编辑器'''

'''Copyright(c)'''
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from tkinter.scrolledtext import *
from tkinter.simpledialog import *
from tkinter.ttk import *

import sys
import os
import requests # 网络爬虫分析，用来检测版本
import webbrowser # 更新网站
import random # 激活码

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def openfile():
    openfilename = askopenfilename()
    if openfilename == '':
        return
    with open(openfilename, encoding = 'UTF-8') as file:
        connect = file.read()
    text_edit.delete('1.0', END)
    text_edit.insert(END, connect)
    mainwindow.title(openfilename + '中文版IDLE文件打开')
    file.close()

def newfile():
    text_edit.delete(1.0, END)
    mainwindow.title('中文版IDLE')

def savefile():
    savefilename = asksaveasfilename(filetypes = [('Python文件', '.py'), ('所有文件', '.*')])
    if savefilename == '':
        return
    with open(savefilename, 'w', encoding = 'UTF-8') as file:
        file.write(text_edit.get(1.0,END))
        file.close()

def open_module():
    pass

def undo():
    try:
        text_edit.edit_undo()
    except:
        showinfo('提示', '您现在无法进行复原动作。因为先前没有动作。')

def redo():
    try:
        text_edit.edit_redo()
    except:
        showinfo('提示', '您现在无法进行重做动作。因为先前没有动作。')

def cut():
    text_edit.event_generate('<<Cut>>')

def copy():
    text_edit.event_generate('<<Copy>>')

def paste():
    text_edit.event_generate('<<Paste>>')

def helping():
    showinfo(message = '这部分内容没有被开发出来。')

def about_soft():
    showinfo('关于中文版IDLE', '中文版IDLE\n版本1.0\n版权所有')

def update():
    try:
        update_date = requests.get('https://zhihongwang250.github.io/programme_install_webside')
        if update_date.status_code == requests.codes.ok:
            if 'version=1.0;' not in update_date:
                askquestion('安装更新', '检测到了新版本，是否更新？')
            else:
                showinfo('安装更新', '已经是最新版本')
        else:
            showerror('安装更新', '网络异常或连接失败')
    except:
        showerror('安装更新', '无法正常安装更新')

def openurl():
    webbrowser.open('https://zhihongwang250.github.io/programme_install_webside')

def font():
    pass

def size():
    pass

def ok():
    with open('data.txt', encoding = 'UTF-8') as file:
        file.write(strtext)

def start_first():
    global strtext
    sf = Toplevel()
    sf.title('欢迎使用中文版IDLE')
    Label(sf, text = '欢迎使用！\n我们现在做点设置就可以了。').pack()
    lf = LabelFrame(sf)
    Label(lf, text = '您想要什么字体？').pack()
    font = Entry(lf)
    font.pack()
    Label(lf, text = '字体的大小是什么？（只能填数字）').pack()
    size = Entry(lf)
    size.pack()
    Label(lf, text = '背景颜色是什么？（英文颜色名）').pack()
    bg = Entry(lf)
    bg.pack()
    bg.insert(1, 'white')
    strtext = 'font = {}\nsize = {}\nbg = {}\nuse = 1'.format(font.get(), size.get(), bg.get())
    Button(lf, text = '确定', command = ok).pack()
    lf.pack()

def show(event):
    num = text_edit.index("insert")
    if event.keycode == 13:
        num =float(num) + 1
    lc.set("行数:{} 字符数:{}".format(*str(num).split('.')))

def send():
    code = random.randint(10000, 99999)
    message = MIMEText('您的激活码是{}'.format(code),' plain', 'utf-8')
    message['Subject'] = '中文版IDLE激活码' 
    message['From'] =  'zqtang10@qq.com'
    message['To'] = e_mail.get()

    try:
        server = smtplib.SMTP('smtp.qq.com')
        server.login('zqtang10@qq.com', 'ikujwrgiwifychcg')
        server.sendmail('zqtang10@qq.com', e_mail.get(), message.as_string())
        showinfo(message = '邮件发送成功。')
        server.quit()
    except Exception as e:
        showerror(message = '发送邮件时出现异常，请重试。\n{}'.format(e))
    else:
        code_name = askstring('激活码输入', '请输入您获得的激活码')
        if not code_name:
            return

        if code_name == code:
            showinfo(message = '激活成功！')
        else:
            showerror(message = '激活失败！\n您可能：\n输入了错误的激活码。')
def jihuo_mainwindow():
    global e_mail
    jh = Toplevel()
    jh.title('激活')
    Label(jh, text = '您的中文版IDLE程序需要激活。\n请先输入您的邮箱，我们会发电子邮件过去。').pack()
    e_mail = Entry(jh)
    e_mail.pack()
    Button(jh, text = '发送验证码', command = send).pack()
    Label(jh, text = '就绪').pack(side = 'right')

def close():
    sys.exit()

# 主窗口
mainwindow = Tk()
mainwindow.title('中文版IDLE')

# 菜单控件的对象名
mainmenu = Menu(mainwindow)
file = Menu(mainmenu, tearoff = 0)
edit  = Menu(mainmenu, tearoff = 0)
about = Menu(mainwindow, tearoff = 0)
gexinghua = Menu(mainmenu, tearoff = 0)
updatemenu = Menu(mainwindow, tearoff = 0)

# 文件编辑菜单
mainmenu.add_cascade(label = '文件', menu = file)
file.add_command(label =  '新建文件', command = newfile)
file.add_command(label = '打开文件', command = openfile)
file.add_command(label = '保存文件', command = savefile)
file.add_command(label = '打开Python代码库', command = open_module)
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
mainwindow.config(menu = mainmenu)

# 个性化菜单
mainmenu.add_cascade(label = '个性化', menu = gexinghua)
gexinghua.add_command(label = '字体设置', command = font)
gexinghua.add_command(label = '大小设置', command = size)
mainwindow.config(menu = mainmenu)

# 帮助菜单
mainmenu.add_cascade(label = '帮助', menu = about)
about.add_command(label = '查看帮助', command = helping)
about.add_separator()
about.add_command(label = '关于中文版IDLE', command = about_soft)
about.add_cascade(label = '更新', menu = update)
updatemenu.add_command(label = '检查更新', command = update)
updatemenu.add_command(label = '转到更新网站', command = openurl)
mainwindow.config(menu = mainmenu)

text_edit = ScrolledText(mainwindow, undo = True)
text_edit.pack()
text_edit.bind('<KeyPress>', show)

lc = StringVar(mainwindow)
lncol = Label(mainwindow, textvariable = lc)
lncol.pack(side = 'right')
lc.set('行号:0 字符数:0')

fileopen = open('data.txt', encoding ='UTF-8')
a = fileopen.read()
if 'use = 0' in a:
    start_first()
if 'sing = 0' in a:
    jihuo_mainwindow()
# 启动事件主循环
try:
    mainwindow.mainloop()
except KeyboardInterrupt:
    pass
else:
    pass