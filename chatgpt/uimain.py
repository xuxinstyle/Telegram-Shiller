import tkinter as tk

root = tk.Tk()
root.title("My GUI")

# 创建菜单栏
menu_bar = tk.Menu(root)

# 创建文件菜单和帮助菜单
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open")
file_menu.add_command(label="Save")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About")
menu_bar.add_cascade(label="Help", menu=help_menu)

root.config(menu=menu_bar)

# 创建标签和按钮
label = tk.Label(root, text="Welcome to My GUI!")
label.pack(pady=10)

button1 = tk.Button(root, text="Button 1")
button1.pack(pady=5)

button2 = tk.Button(root, text="Button 2")
button2.pack(pady=5)

button3 = tk.Button(root, text="Button 3")
button3.pack(pady=5)

# 设置窗口尺寸和位置
window_width = 400
window_height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = int((screen_width - window_width) / 2)
y = int((screen_height - window_height) / 2)
root.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))

root.mainloop()