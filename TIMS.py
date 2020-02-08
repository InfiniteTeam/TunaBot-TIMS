import tkinter as tk
from tkinter import ttk

window = tk.Tk()

# 창 기본 설정
window.title('TIMS - 참치봇 통합 관리 시스템')
window.geometry('960x540+200+200')
window.resizable(False, False)

# 상단 배너 설정
img = tk.PhotoImage(file='./resources/tims-label.png')
LabelBanner = tk.Label(window, image=img)
LabelBanner.place(x=-5, y=0)

# 봇 시작 버튼 설정
style = ttk.Style()
style.configure('TButton', width=20)

ButtonBotStart = ttk.Button(window, text="봇 시작", style='TButton')
ButtonBotStart.place(x=0, y=30)

# 봇 로그 상자 설정
TextBotLog = tk.Text(window)
TextBotLog.insert(tk.CURRENT, 'ㅎㅇㅎㅇ\n')
TextBotLog.config(state='disable')
TextBotLog.pack()

window.mainloop()