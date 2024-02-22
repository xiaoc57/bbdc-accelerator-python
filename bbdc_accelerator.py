import pyautogui
import json
from pynput import mouse, keyboard
import keyboard as kd

# 读取配置文件
try:
    with open('bbdc_config.json', 'r', encoding='utf-8') as file:
        config = json.load(file)
except Exception as e:
    print("读取配置文件失败！", e)
    exit()

window_title = config["window_title"]

# 获取当前活动窗口的左上角坐标和宽高
window = pyautogui.getWindowsWithTitle(window_title)[0]
window_left = window.left
window_top = window.top
window_width = window.width
window_height = window.height
print("窗口左上角坐标(x, y):", window_left, window_top)
print("窗口尺寸(w, h):", window_width, window_height)

button_list = ["left_button", "middle_button", "right_button", "next_button"]
button_positions = {}

mouse_controller = mouse.Controller()

def on_press(key):
    try:
        if key.char == config["confirm"]:  # 检查是否是确认键
            # 获取当前鼠标位置
            x, y = mouse_controller.position
            # 计算相对于窗口的位置
            relative_x, relative_y = x - window_left, y - window_top
            button_positions[current_button] = [relative_x, relative_y]
            print(f"{current_button}位置：", button_positions[current_button])
            return False  # 停止监听
    except AttributeError:
        pass  # 忽略其他按键事件

# 循环每个按钮，提示用户操作
if config["configuration"]:
    for b in button_list:
        current_button = b
        print(f"请将鼠标放在{b}上，并按下{config['confirm']}确认。")
        # 监听键盘事件来获取按钮位置
        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()  # 等待按键确认
        config[b]["location"] = button_positions[b]
        config[b]["status"] = False
else:
    for b in button_list:
        # 强制更新单个按钮状态
        if config[b]["status"]:
            current_button = b
            print(f"请将鼠标放在{b}上，并按下{config['confirm']}确认。")
            # 监听键盘事件来获取按钮位置
            with keyboard.Listener(on_press=on_press) as listener:
                listener.join()  # 等待按键确认
            config[b]["location"] = button_positions[b]
            config[b]["status"] = False
config["configuration"] = False

# 将config存回
# 将更新后的配置保存回文件
try:
    with open('bbdc_config.json', 'w', encoding='utf-8') as file:
        json.dump(config, file, ensure_ascii=False, indent=4)
    print("配置文件保存成功！")
except Exception as e:
    print("保存配置文件失败！", e)

# 按照按钮点击即可
def click(x, y):
    pyautogui.moveTo(window.left + x, window.top + y)
    pyautogui.click()

# button_list = ["left_button", "middle_button", "right_button", "next_button"] 

def on_key_press(event):
    for l in range(len(button_list)):
        if event.name == config[button_list[l]]["key"]:
            click(config[button_list[l]]["location"][0], config[button_list[l]]["location"][1])

kd.on_press(on_key_press)

print("程序运行中...按下'ctrl-c'退出。")

while True:
    
    pass

