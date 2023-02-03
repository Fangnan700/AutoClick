import time

import keyboard
import subprocess


def func():
    global process
    process = subprocess.Popen([r'.\venv\Scripts\python.exe', 'script.py'])
    print('开始运行...')


def stop_func():
    # 终止函数
    global process
    if process != subprocess.PIPE:
        process.terminate()
        print('终止运行...')
    else:
        pass


keyboard.add_hotkey("pagedown", func)
keyboard.add_hotkey("pageup", stop_func)
process = subprocess.PIPE

print('按下 Page-down 键开始运行，按下 Page-up 键终止运行')
while True:
    keyboard.wait()
    time.sleep(5)
