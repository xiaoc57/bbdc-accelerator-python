# bbdc-accelerator-python

这个项目是对 [bbdc-accelerator](https://github.com/KermanX/bbdc-accelerator) 这个项目的扩展。

1. 不背单词app（WSA 环境下）快捷键支持。能极大提高背单词时的点击效率。

2. 我有一根ppt的笔，上下键能够很好的控制常用的选项（认识或不认识）。我经常在mac上的安卓模拟器使用这根笔。能够提升点击效率（自我感觉）。

3. 还有一点是我不太会写Windows平台上的c++。

## 安装说明

1. 首先运行不背单词模拟器窗口，wsa也可，模拟器应该也可（没做测试）。

2. 根据屏幕提示调整几个按键的位置

3. 开始使用

## 使用说明

    python = 3.9, 可用以下方法配置环境
    conda create -n bbdc python=3.9
    conda activate bbdc
    pip install -r requirements.txt

### 本程序提供的快捷键

    快捷键在bbdc_config中定义，每个字段的意义如下：
    - "window_title": 窗口名称
    - "configuration": 是否重新确认按钮
    - "confirm": 确认键
    共定义了四个按钮，因为我的笔上一共就四个按键，建议不要使用enter键，next_button表示学习下一组词，其他为字面意思。
    - "describe": 描述,
    - "key": 键位,
    - "location": 与左上角的相对位置
    - "status": true为强制更新单个按钮的位置

# 如果有任何疑问，欢迎issue！
# 可去原作者处star, 好像只有我star了。