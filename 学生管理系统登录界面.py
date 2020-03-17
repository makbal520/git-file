# -*- coding: utf-8 -*-
"""
Created on Sat May 25 16:59:49 2019

@author: 15299
"""




import tkinter as tk
import tkinter.messagebox
from tkinter import simpledialog


 
window = tk.Tk()
window.title("学生管理系统登录界面")
window.geometry("500x400")
 
 
tk.Label(window, text='用户名:').place(x=50, y=200)
tk.Label(window, text='密码:').place(x=50, y=250)
 
var_usr_name = tk.StringVar()
var_usr_name.set('')
entry_usr_name = tk.Entry(window, textvariable=var_usr_name)
entry_usr_name.place(x=160, y=200)

 
var_usr_pwd = tk.StringVar()
entry_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd, show='*')
entry_usr_pwd.place(x=160, y=250)

teacher_account={'admin':{'Pwd':'123456',
                          'Name':'Admin'},
                 'admin2':{'Pwd':'987654321',
                           'Name':'Admin2'}}
student_list={'BZB':100,
              'bzb':80,
              'Bzb':95}

def add_chengji():
    n=tk.simpledialog.askstring('提示','请输入学生姓名')
    if n in student_list:
        tk.messagebox.showerror(message="该学生已存在")
    else:
        add_score=simpledialog.askinteger('提示','请输入学生成绩',minvalue=1,maxvalue=100)
        student_list.setdefault(n,add_score)


btn_tuichu = tk.Button(window, text="退出", command=window.destroy)
btn_tuichu.place(x=250, y=300)
btn_login = tk.Button(window, text="Login", command=usr_login)
btn_login.place(x=155, y=300)
window.mainloop()


    