import tkinter as tk
from tkinter import ttk

window = tk.Tk()

# 창 기본 설정
window.title('TIMS - 참치봇 통합 관리 시스템')
window.geometry('960x540+200+200')
window.resizable(False, False)

# 탭 설정
NotebookTabs = ttk.Notebook(window, width=600, height=400)
NotebookTabs.place(x=350, y=40)

# 봇 로그 탭(Notebook1) 추가
Notebook1 = tk.Frame(window)
NotebookTabs.add(Notebook1, text="봇 로그")
TextBotLog = tk.Text(Notebook1, width=600, height=400)
for x in range(40):
    TextBotLog.insert(tk.CURRENT, "SANS\n")
TextBotLog.config(state='disabled')
TextBotLog.pack()

# 상단 배너 설정
img = tk.PhotoImage(file='./resources/tims-label.png')
LabelBanner = tk.Label(window, image=img)
LabelBanner.place(x=-5, y=0)

# 봇 시작 버튼 설정
style = ttk.Style()
style.configure('TButton', width=20)

ButtonBotStart = ttk.Button(window, text="봇 시작", style='TButton')
ButtonBotStart.place(x=0, y=30)

window.mainloop()