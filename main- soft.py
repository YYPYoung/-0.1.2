import os
import sys
import tkinter as tk
import tkinter.dialog as TkDialog
import tkinter.messagebox as TkMessaeBox
import multiprocessing
import pickle
import webbrowser
from PIL import Image, ImageTk
from tkinter import PhotoImage
from tkinter import filedialog

__version__ = '0.1.2'
__zhanghao__ = "yangyp2013@126.com"
__password__ = "YiZhanDacom"
__sitting__ = {}

sipteacheWeb = "https://espace.sipedu.cn/portalweb/#/"
vipWeb = "https://web.u-p.vip/"
ailpayWeb = "https://i.postimg.cc/D04ngxC3/alipay.gif"
wechatPayWeb = "https://i.postimg.cc/q77RKxd4/wechat-Pay.png"

def save_sittings(dictionary, file_path):
    with open(file_path, 'wb') as file:
        pickle.dump(dictionary, file)

__sitting__.clear()

def load_sittings(file_path):
    with open(file_path, 'rb') as file:
        dictionary = pickle.load(file)
    return dictionary

sitting = load_sittings('sittings.pickle')

def botton(roottk):
    tk.Button(roottk, text="打开一站达/Open One Stop", command=web, height=7, width=52).grid(column=0, row=0, padx=5, pady=5)
    tk.Button(roottk, text="获取账号和密码/Get account and password", command=account, height=7, width=52).grid(column=0, row=1, padx=5, pady=5)
    tk.Button(roottk, text="一键复制/Copy account and password", command=newwindow, height=7, width=52).grid(column=0, row=2, padx=5, pady=5)
    #tk.Button(roottk, text = '退出/Quit', command=os.system('pause'), height=7, width=52).grid(column=0, row=2, padx=5, pady=5)

def setting():
    window = tk.Tk()
    window.title('基本设定/Basic settings')
    window.geometry('400x200')
    var = tk.StringVar()
    l = tk.Label(window, text='主题颜色/Theme colors')
    l.pack()
    r1 = tk.Radiobutton(window, text='浅色',variable=var, value='A',command=lidhtColour)
    r1.pack()
    r2 = tk.Radiobutton(window, text='深色',variable=var, value='B',command=darkColour)
    r2.pack()
    r3 = tk.Radiobutton(window, text='跟随系统',variable=var, value='C',command=systemClolour)
    r3.pack()
    window.mainloop()

def darkColour():
    __sitting__ = {'Colour': '1'}
    saveOver()
    sittingOK()

def lidhtColour():
    __sitting__ = {'Colour': '0'}
    saveOver()
    sittingOK()

def systemClolour():
    __sitting__ = {'Colour': '2'}
    saveOver()
    sittingOK()

def saveOver():
    save_sittings(__sitting__, 'sittings.pickle')
    print(__sitting__)

def nowork():
    TkMessaeBox.showinfo(title="错误",message="功能正在开发，敬请期待")

def sittingOK():
    TkMessaeBox.showinfo(title="设定",message="已完成设定，重启后生效")

def alipay():
    webbrowser.open(ailpayWeb)


def wechatpay():
    webbrowser.open(wechatPayWeb)

def account():
    TkMessaeBox.showinfo(title="账号与密码",message="账号为：yangyp2013@126.com  密码为：YiZhanDacom")

def feedback():
    TkMessaeBox.showinfo(title="反馈",message="如您有宝贵意见欢迎反馈，邮箱：yangyp2013@126.com")

def newwindow():
    window = tk.Tk()
    window.title('一键复制')
    window.resizable(0, 0)
    tk.Button(window, text="复制账号/Copy accout", command=copyAccout, height=7, width=52).grid(column=0, row=0, padx=5, pady=5)
    tk.Button(window, text="复制密码/Copy password", command=copyPassword, height=7, width=52).grid(column=0, row=1, padx=5, pady=5)

def copyAccout():
    rootTk.clipboard_clear()
    rootTk.clipboard_append(__zhanghao__)
    rootTk.update()

def copyPassword():
    rootTk.clipboard_clear()
    rootTk.clipboard_append(__password__)
    rootTk.update()

def web():
    webbrowser.open(vipWeb) # 在默认浏览器中打开 URL
    #webbrowser.open_new_tab(url) # 在新标签页中打开 URL
    #webbrowser.open_new(url) # 在新窗口中打开 URL

def sipteache():
    webbrowser.open(sipteacheWeb)
    TkMessaeBox.showinfo(title="提示",message="易家学院已经停止更新，建议您前往新网站,网址为：https://web.u-p.vip/")

def about():
    TkMessaeBox.showinfo(title="关于软件",message="本软件由一站达官方开发，喜欢本站欢迎赞助")

def version():
    TkMessaeBox.showinfo(title="版本",message="版本为：{}".format(__version__))

def bar(rootTk):
    menuBar = tk.Menu(rootTk)

    #第一个菜单
    menu1 = tk.Menu(menuBar, tearoff=0)
    menu1.add_command(label="基础设定/Basic settings", command=nowork)
    menuBar.add_cascade(label="设置/Set up", menu=menu1)
    #第二个菜单
    menu2 = tk.Menu(menuBar, tearoff=0)
    menu2.add_command(label="信息/Information", command=about)
    menu2.add_command(label="版本/Version", command=version)
    menu2.add_command(label="反馈/Feedback", command=feedback)
    menuBar.add_cascade(label="关于/About", menu=menu2)
    #第三个菜单
    menu3 = tk.Menu(menuBar, tearoff=0)
    menu3.add_command(label="支付宝/Alipay", command=alipay)
    menu3.add_command(label="微信支付/Wechat Pay", command=wechatpay)
    menuBar.add_cascade(label="赞助/Sponsor", menu=menu3)
    #第四个菜单
    menu4 = tk.Menu(menuBar, tearoff=0)
    menu4.add_command(label="旧版一站达（易家学院）", command=sipteache)
    menuBar.add_cascade(label="更多/More", menu=menu4)

    rootTk.config(menu=menuBar)

if __name__ == "__main__":  # pragma: no cover
    if sys.platform.startswith('win'):
        multiprocessing.freeze_support()
    rootTk = tk.Tk()
    rootTk.title("一站达启动器")
    rootTk.geometry("400x430")
    rootTk.resizable(0, 0) #禁止调整大小
    bar(rootTk)
    botton(rootTk)
    rootTk.mainloop()