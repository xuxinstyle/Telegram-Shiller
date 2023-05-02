import tkinter as tk

class MyUI:
    def __init__(self, master):
        self.master = master
        self.master.title("My UI")

        # 创建左侧框架
        self.left_frame = tk.Frame(self.master)
        self.left_frame.pack(side=tk.LEFT)

        # 创建右侧框架
        self.right_frame = tk.Frame(self.master)
        self.right_frame.pack(side=tk.LEFT)

        # 创建按钮
        self.button1 = tk.Button(self.left_frame, text="Button 1", command=self.button1_clicked)
        self.button2 = tk.Button(self.left_frame, text="Button 2", command=self.button2_clicked)
        self.button3 = tk.Button(self.left_frame, text="Button 3", command=self.button3_clicked)

        # 将按钮放在左侧框架中
        self.button1.pack()
        self.button2.pack()
        self.button3.pack()

        # 创建文本框
        self.text_box = tk.Text(self.right_frame, height=10, width=50)

        # 将文本框放在右侧框架中
        self.text_box.pack()

    def button1_clicked(self):
        self.text_box.insert(tk.END, "Button 1 clicked.\n")

    def button2_clicked(self):
        self.text_box.insert(tk.END, "Button 2 clicked.\n")

    def button3_clicked(self):
        self.text_box.insert(tk.END, "Button 3 clicked.\n")

if __name__ == '__main__':
    root = tk.Tk()
    app = MyUI(root)
    root.mainloop()