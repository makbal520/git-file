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
def search():
    for i in student_list:
        print('姓名'+i+' '+'成绩'+str(student_list[i]))
def usr_login():
    # 这两行代码就是获取用户输入的usr_name和usr_pwd
    usr_name = var_usr_name.get()
    usr_pwd = var_usr_pwd.get()
    t1=teacher_account.get('admin').get('Name')+teacher_account.get('admin2').get('Name')
    t2=teacher_account.get('admin').get('Pwd')+teacher_account.get('admin2').get('Pwd')

    if usr_name in t1 and usr_pwd in t2:
        yes=tk.Tk()
        tk.messagebox.showinfo(title="欢迎", message="欢迎，教师" + usr_name)
        window.exits()
        def creat1():
            root = tk.Tk()
            root.title('学生管理系统')
            yes.exits()         
            def creat2():
                root.exits()
            tk.Button(root, text='添加成绩', width=6, command=add_chengji).pack()
            tk.Button(root, text='查看成绩', width=6, command=search).pack()
            tk.Button(root, text='退出', width=6, command=creat2).pack()
        tk.Button(yes,text='确定',command=creat1).pack()
    else:
        tk.messagebox.showerror(message="用户名或密码错误")
def exits():
    root.destroy()    
#定义关闭窗口的函数
btn_tuichu = tk.Button(window, text="退出", command=window.destroy)
btn_tuichu.place(x=250, y=300)
btn_login = tk.Button(window, text="Login", command=usr_login)
btn_login.place(x=155, y=300)
window.mainloop()



    