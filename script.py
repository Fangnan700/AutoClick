import sys
import pyautogui
import time

# 函数实现
time.sleep(1)
print('开始执行')
# 步骤1 - 社会保障号
pyautogui.click(240, 160)
print('步骤1 - 社会保障号')
time.sleep(1)

# 步骤2 - 保存
pyautogui.click(770, 710)
print('步骤2 - 保存')
time.sleep(3)

# 步骤3 - 确定保存
pyautogui.click(980, 590)
print('步骤3 - 确定保存')
time.sleep(1)

# 步骤4 - 核准
pyautogui.click(890, 710)
print('步骤4 - 核准')
time.sleep(1)

# 步骤5 - z实指数
pyautogui.click(715, 440)
print('步骤5 - z实指数')
time.sleep(1)

# 步骤6 - 与社保同步
pyautogui.click(650, 310)
print('步骤6 - 与社保同步')
time.sleep(1)

# 步骤7 - 计算
pyautogui.click(540, 780)
print('步骤7 - 计算')
time.sleep(1)

# 步骤8 - 退出
pyautogui.click(1165, 308)
print('步骤8 - 退出')
time.sleep(1)

# 步骤9 - 确定保存
pyautogui.click(930, 590)
print('步骤9 - 确定保存')
time.sleep(1)

# 步骤10 - 计算
pyautogui.click(720, 745)
print('步骤10 - 计算')
time.sleep(1)

# 步骤11 - 保存修改信息
pyautogui.click(720, 745)
print('步骤11 - 保存修改信息')
time.sleep(1)

# 步骤12 - 确定保存
pyautogui.click(1045, 600)
print('步骤12 - 确定保存')
print('执行结束')
sys.exit(0)

