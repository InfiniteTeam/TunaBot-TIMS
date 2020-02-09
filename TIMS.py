import tkinter as tk
from tkinter import ttk, font, filedialog, messagebox
import threading
import os, platform, sys
import discord

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
LabelBotToken.place(x=10, y=90)

# 봇 토큰 입력칸 설정
EntryBotToken = ttk.Entry(window, show='●')
EntryBotToken.place(x=80, y=90, width=162)

# 봇이 여기서 실질적으로 실행됩니다.
'''
    if platform.system() == 'Windows':
        os.system('cd {}'.format(os.getcwd()))
        output = os.popen('python _bot.py').read()
        TextBotLog.config(state='normal')
        TextBotLog.insert(tk.END, output)
        TextBotLog.config(state='normal')
'''
client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    await client.change_presence(status=discord.Status.dnd, activity=discord.Game('InfinieTEAM'))

@client.event
async def on_message(message):
    if message.content.startswith('hu'):
        await message.channel.send('dwdw')

def botThread():
    client.run(EntryBotToken.get())

# 봇 실행 사전 준비
def botStart():
    ButtonBotStart.config(state='disabled')
    if EntryBotToken.get():
        threading.Thread(target=botThread,
                         daemon=True).start()  # 봇 소스 파일이 실행되는 동안 프로그램 진행이 멈추고 응답 없음이 되므로, 멀티스레딩으로 해결.
    else:
        messagebox.showerror('토큰 오류', '토큰을 입력하세요')

def botStop():
    pass

# 봇 시작 버튼 설정
ButtonBotStart = ttk.Button(window, text="봇 시작", command=botStart)
ButtonBotStart.place(x=10, y=118, width=113)

# 봇 정지 버튼 설정
ButtonBotStop = ttk.Button(window, text="봇 정지", command=botStop)
ButtonBotStop.place(x=130, y=118, width=113)

# 창이 닫힐 때 알림상자.
def onClosing():
    if str(ButtonBotStart['state']) == 'disabled':
        if messagebox.askyesno('종료', '현재 봇 세션이 실행중입니다. 지금 닫으면 세션을 강제 종료하게 됩니다. 봇 종료를 통해 안전하게 종료한 후 닫는 것을 권장합니다.'):
            sys.exit()
    else:
        window.destroy()

window.protocol('WM_DELETE_WINDOW', onClosing)
window.mainloop()