# サンプルコード
import tkinter as tk
from tkinter import ttk

# 列の識別名を指定
column = ('ID', 'Name', 'Score')
# メインウィンドウの生成
root = tk.Tk()
root.title('Score List')
root.geometry('400x300')
# Treeviewの生成
tree = ttk.Treeview(root, columns=column)
# 列の設定
tree.column('#0',width=0, stretch='no')
tree.column('ID', anchor='center', width=80)
tree.column('Name',anchor='w', width=100)
tree.column('Score', anchor='center', width=80)
# 列の見出し設定
tree.heading('#0',text='')
tree.heading('ID', text='ID',anchor='center')
tree.heading('Name', text='Name', anchor='w')
tree.heading('Score',text='Score', anchor='center')
# レコードの追加
tree.insert(parent='', index='end', iid=0 ,values=(1, 'KAWASAKI',80))
tree.insert(parent='', index='end', iid=1 ,values=(2,'SHIMIZU', 90))
tree.insert(parent='', index='end', iid=2, values=(3,'TANAKA', 45))
tree.insert(parent='', index='end', iid=3, values=(4,'OKABE', 60))
tree.insert(parent='', index='end', iid=4, values=(5,'MIYAZAKI', 99))
# ウィジェットの配置
tree.pack(pady=10)

root.mainloop()