import tkinter as tk
from tkinter import ttk, font, filedialog

window = tk.Tk()

# 창 기본 설정
window.title('TIMS - 참치봇 통합 관리 시스템')
window.geometry('960x540+200+200')
window.resizable(False, False)

# 탭 설정
NotebookTabs = ttk.Notebook(window, width=700, height=430)
NotebookTabs.place(x=250, y=40)

# 봇 로그 탭(Notebook1) 추가
Notebook1 = tk.Frame(window)
NotebookTabs.add(Notebook1, text="봇 로그")
TextBotLog = tk.Text(Notebook1, width=700, height=430)
for x in range(40):
    TextBotLog.insert(tk.CURRENT, "SANS\n")
TextBotLog.config(state='disabled')
TextBotLog.pack()

# 상단 배너 설정
imgLabelBanner = tk.PhotoImage(file='./resources/tims-label.png')
LabelBanner = tk.Label(window, image=imgLabelBanner)
LabelBanner.place(x=-5, y=0)

# 좌측 로고 설정
imgLabelLogo = tk.PhotoImage(file='./resources/TunaBot-text.png')
LabelLogo = tk.Label(window, image=imgLabelLogo)
LabelLogo.place(x=5, y=35)

# 좌측 로고 By InfiniteTEAM 설정
font = tk.font.Font(family='맑은 고딕', size=11)
LabelBy = tk.Label(window, text='By InfiniteTEAM', font=font)
LabelBy.place(x=110, y=50)

# 봇 토큰 라벨 설정
LabelBotToken = tk.Label(window, text='봇 토큰:')
LabelBotToken.place(x=10, y=80)

# 봇 토큰 입력칸 설정
EntryBotToken = ttk.Entry(window, width=22, show='●')
EntryBotToken.place(x=80, y=80)

# 봇 소스 경로 라벨 설정
LabelBotSource = tk.Label(window, text='봇 소스:')
LabelBotSource.place(x=10, y=110)

# 봇 소스 경로 입력칸 설정
EntryBotSource = ttk.Entry(window, width=18)
v = tk.StringVar()
EntryBotSource.config(textvariable=v)
EntryBotSource.place(x=80, y=110)

def openFileDialog():
    file = tk.filedialog.askopenfile(window)
    EntryBotSource.delete(0, tk.END)
    v.set(file)

# 봇 소스 경로 선택창 열기 버튼
ButtonBotSource = ttk.Button(window, text='...', command=openFileDialog)
ButtonBotSource.place(x=215, y=110, width= 26, height=21)

# 봇 시작 버튼 설정
style = ttk.Style()
style.configure('TButton', width=20)

ButtonBotStart = ttk.Button(window, text="봇 시작", style='TButton')
#ButtonBotStart.place(x=0, y=70)

window.mainloop()