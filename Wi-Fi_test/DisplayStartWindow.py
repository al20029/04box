import tkinter
import tkinter.ttk as ttk
from ToolTip import *


    
def btn_click():
    frm.destroy()

# Tkクラス生成
frm = tkinter.Tk()
# 画面サイズ
frm.geometry('500x270')
# 画面タイトル
frm.title('計測開始画面')
chk1 = tkinter.Label(frm,text='Wi-Fi速度計測システム',font = ('MSゴシック',35))
chk1.place(x = 15, y = 85)
bln = tkinter.BooleanVar()
bln.set(True)
chk2 = tkinter.Checkbutton(frm, variable=bln, text='定期計測を利用する',font = ('MSゴシック',10))
chk2.place(x=270, y=30)
chk4 = tkinter.Label(frm,text='?',font = ('MSゴシック',10))
chk4.place(x=410, y=30)

list = ("AAA", "BBB", "CCC")


combobox = ttk.Combobox(frm, height=3, values = list,state = "readonly")
combobox.place(x = 100, y = 200)

# 画面をそのまま表示
btn = tkinter.Button(frm, text='計測開始',width = 18,height = 2,command = btn_click,bg='#808080',font = ('MSゴシック', 10))
btn.place(x=330, y=200)

ToolTip(chk4,"ツールチップ")
frm.mainloop()